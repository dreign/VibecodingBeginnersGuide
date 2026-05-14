#!/usr/bin/env python3
"""
批量将第 2~16 章目录中的 .md 文件转换为 .html 文件。
复用 style.css，在图片位置插入占位符。
"""

import os
import re

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 各章主题色配置
CHAPTER_THEMES = {
    "01": {"primary": "#5a6a7a", "secondary": "#88a8b8"},
    "02": {"primary": "#6a7a8a", "secondary": "#98a8b8"},
    "03": {"primary": "#7a8a6a", "secondary": "#a8b898"},
    "04": {"primary": "#8a6a7a", "secondary": "#b898a8"},
    "05": {"primary": "#6a8a7a", "secondary": "#98b8a8"},
    "06": {"primary": "#8a7a6a", "secondary": "#b8a898"},
    "07": {"primary": "#7a6a8a", "secondary": "#a898b8"},
    "08": {"primary": "#6a7a8a", "secondary": "#98a8b8"},
    "09": {"primary": "#7a8a6a", "secondary": "#a8b898"},
    "10": {"primary": "#8a6a7a", "secondary": "#b898a8"},
    "11": {"primary": "#6a8a7a", "secondary": "#98b8a8"},
    "12": {"primary": "#8a7a6a", "secondary": "#b8a898"},
    "13": {"primary": "#7a6a8a", "secondary": "#a898b8"},
    "14": {"primary": "#6a7a8a", "secondary": "#98a8b8"},
    "15": {"primary": "#7a8a6a", "secondary": "#a8b898"},
    "16": {"primary": "#8a6a7a", "secondary": "#b898a8"},
}

# 要处理的章节目录
CHAPTER_DIRS = [
    "01-时代背景",
    "02-生产关系的演变",
    "03-生产工具的演变",
    "04-传统开发生命周期回顾",
    "05-一人公司",
    "06-Token即流量",
    "07-Vibe-Coding核心概念",
    "08-从Vibe-Coding到Vibe-Learning",
    "09-大模型",
    "10-工具生态全景",
    "11-环境及工具配置详解",
    "12-第一个应用",
    "13-进阶实战项目库",
    "14-开源库",
    "15-软件的背后",
    "16-附录",
]


def get_chapter_number(dirname):
    """从目录名提取章节号（如 '02-...' -> '02'）"""
    m = re.match(r"(\d+)", dirname)
    return m.group(1) if m else None


def extract_title(md_lines):
    """从 MD 内容中提取标题（第一个 ## 行）"""
    for line in md_lines:
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            return m.group(1).strip()
    return ""


def extract_meta(md_content):
    """提取 HTML 注释中的元数据"""
    m = re.search(r"<!--\s*\n(.*?)-->", md_content, re.DOTALL)
    if m:
        text = m.group(1).strip()
        return text.replace("\n", "<br>")
    return ""


def inline_format(text):
    """处理行内格式：**bold**、`code`、链接"""
    # **bold** → <strong>
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # `code` → <code>
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # [text](url) → <a href="url">text</a>
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def generate_inline_style(theme):
    """生成内联主题样式（仅保留每章主题色变量）"""
    p = theme["primary"]
    s = theme["secondary"]
    return f"""body::before {{
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, {p}, {s}, {p});
    z-index: 100;
  }}
  .chapter-meta {{ color: {p}; }}
  .title-divider {{ background: {s}; }}
  strong {{ color: {p}; }}
  .img-icon {{ color: {s}; }}
  .img-label {{ color: {p}; }}
  .img-caption {{ color: {p}; }}
  .takeaways-title {{ color: {p}; }}
  .takeaways li::before {{ color: {s}; }}
  .vibe-label {{ color: {p}; }}
  .vibe-prompt::before {{ color: {s}; }}
  blockquote {{ border-left-color: {s}; }}
  th {{ color: {p}; }}"""


def generate_html(md_path, rel_dir):
    """将单个 MD 文件转换为 HTML 内容"""
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    lines = md_content.split("\n")

    title = extract_title(lines)
    meta_text = extract_meta(md_content)
    chapter_num = get_chapter_number(rel_dir)
    theme = CHAPTER_THEMES.get(chapter_num, {"primary": "#6a7a8a", "secondary": "#98a8b8"})

    # 移除 HTML 注释块（<!-- ... -->）中的行，避免重复渲染
    cleaned_lines = []
    in_comment = False
    for line in lines:
        if line.strip().startswith("<!--"):
            in_comment = True
            # 如果 --> 在同一行
            if "-->" in line:
                in_comment = False
            continue
        if line.strip().endswith("-->"):
            in_comment = False
            continue
        if not in_comment:
            cleaned_lines.append(line)
    lines = cleaned_lines

    # --- 解析 MD 为 HTML 片段列表 ---
    html_parts = []

    # 如果存在元数据，排第一
    if meta_text:
        html_parts.append(f'<div class="section-meta">{meta_text}</div>')

    in_code_block = False
    code_buffer = []
    in_list = False
    list_type = None          # "ul" or "ol"
    list_buffer = []
    in_takeaways = False
    takeaways_buffer = []
    in_vibe = False
    vibe_buffer = []
    in_blockquote = False
    quote_buffer = []
    last_was_image = False    # 上一行是否是图片，用于捕获图片标题
    img_caption_pending = None  # 图片标题文本
    skipped_first_h2 = False   # 是否已跳过首个 h2（因为已作为页面标题渲染）

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        next_line = lines[i + 1] if i + 1 < len(lines) else ""

        # --- 代码块 ---
        if stripped.startswith("```"):
            if in_code_block:
                # 结束代码块
                in_code_block = False
                code_html = "\n".join(code_buffer)
                html_parts.append(f"<pre><code>{code_html}</code></pre>")
                code_buffer = []
                i += 1
                continue
            else:
                # 开始代码块
                in_code_block = True
                code_buffer = []
                i += 1
                continue

        if in_code_block:
            # 将特殊字符转义
            escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            code_buffer.append(escaped)
            i += 1
            continue

        # --- 水平分隔线 ---
        if stripped == "---" and not in_takeaways and not in_vibe:
            # flush pending image caption first
            if img_caption_pending:
                html_parts.append(f'<div class="img-caption">{inline_format(img_caption_pending)}</div>')
                img_caption_pending = None
            if last_was_image:
                last_was_image = False
            html_parts.append('<div class="title-divider"></div>')
            i += 1
            continue

        # --- 跳过空的 title-divider 行（紧跟在 title-divider 后的空行）---
        # 不需要处理，自然跳过

        # --- 图片占位 ---
        img_match = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if img_match:
            # 先 flush 待处理的图片标题
            if img_caption_pending:
                html_parts.append(f'<div class="img-caption">{inline_format(img_caption_pending)}</div>')
                img_caption_pending = None
            alt_text = img_match.group(1)
            img_src = img_match.group(2)
            html_parts.append(
                f'<div class="img-placeholder">'
                f'<div class="img-icon">🖼</div>'
                f'<div class="img-label">{inline_format(alt_text)}</div>'
                f'</div>'
            )
            last_was_image = True
            i += 1
            continue

        # --- 图片标题（图片后紧跟的 *▲ ...* 行）---
        if last_was_image and re.match(r"^\*.*\*$", stripped):
            caption_content = stripped.strip("*").strip()
            img_caption_pending = caption_content
            last_was_image = False
            i += 1
            continue
        else:
            if last_was_image and img_caption_pending:
                html_parts.append(f'<div class="img-caption">{inline_format(img_caption_pending)}</div>')
                img_caption_pending = None
            last_was_image = False

        # --- 检查特殊区块的开始 ---
        # ## 2.x 或 ### 2.x  这些是普通标题，需要判断是否是特殊区块标题

        # ### 本节要点 → 开启 takeaways
        if re.match(r"^###\s+本节要点", stripped):
            if in_takeaways:
                html_parts.append(f'<div class="takeaways">{chr(10)}{chr(10).join(takeaways_buffer)}{chr(10)}</div>')
                takeaways_buffer = []
                in_takeaways = False
            if in_vibe:
                html_parts.append(render_vibe(vibe_buffer))
                vibe_buffer = []
                in_vibe = False
            in_takeaways = True
            takeaways_buffer.append('<div class="takeaways-title">本节要点</div>')
            i += 1
            continue

        # ### Vibe 练习 → 开启 vibe 区块
        if re.match(r"^###\s+Vibe\s+(练习|日志)", stripped):
            if in_takeaways:
                html_parts.append(f'<div class="takeaways">{chr(10)}{chr(10).join(takeaways_buffer)}{chr(10)}</div>')
                takeaways_buffer = []
                in_takeaways = False
            if in_vibe:
                html_parts.append(render_vibe(vibe_buffer))
                vibe_buffer = []
                in_vibe = False
            in_vibe = True
            # 不直接加内容，等 render 时统一加标题
            i += 1
            continue

        # --- 如果在特殊区块内 ---
        if in_takeaways:
            if not stripped:  # 空行
                i += 1
                continue
            if stripped.startswith("---"):
                # 闭合 <ul>
                if any("<ul>" in l for l in takeaways_buffer) and not any("</ul>" in l for l in takeaways_buffer):
                    takeaways_buffer.append("</ul>")
                html_parts.append(f'<div class="takeaways">{chr(10)}{chr(10).join(takeaways_buffer)}{chr(10)}</div>')
                takeaways_buffer = []
                in_takeaways = False
                html_parts.append('<div class="title-divider"></div>')
                i += 1
                continue
            # 列表项
            if re.match(r"^[-*]\s+", stripped):
                li_content = re.sub(r"^[-*]\s+", "", stripped)
                if not any("<ul>" in l for l in takeaways_buffer):
                    takeaways_buffer.append('<ul>')
                takeaways_buffer.append(f'<li>{inline_format(li_content)}</li>')
                i += 1
                # 继续收集连续列表项
                while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                    li_c = re.sub(r"^[-*]\s+", "", lines[i].strip())
                    takeaways_buffer.append(f'<li>{inline_format(li_c)}</li>')
                    i += 1
                continue
            else:
                # 不是列表的直接文本
                takeaways_buffer.append(f'<p>{inline_format(stripped)}</p>')
                i += 1
                continue

        if in_vibe:
            if not stripped:
                i += 1
                continue
            if stripped.startswith("---"):
                # 闭合 vibe-prompt（如果开启）
                if any("vibe-prompt" in l for l in vibe_buffer):
                    vibe_buffer.append('</div>')
                html_parts.append(render_vibe(vibe_buffer))
                vibe_buffer = []
                in_vibe = False
                html_parts.append('<div class="title-divider"></div>')
                i += 1
                continue
            # 引用块 → vibe-prompt
            if stripped.startswith(">"):
                quote_text = re.sub(r"^>\s*", "", stripped)
                if not any("vibe-prompt" in l for l in vibe_buffer):
                    vibe_buffer.append(f'<div class="vibe-prompt">')
                vibe_buffer.append(f'<p>{inline_format(quote_text)}</p>')
                i += 1
                continue
            # 非引用的直接文本
            # 如果 vibe-prompt 已开启，先关闭它，让后面的文本在 prompt 外面
            prompt_idx = -1
            for idx, v in enumerate(vibe_buffer):
                if "vibe-prompt" in v and "</div>" not in v:
                    prompt_idx = idx
            if prompt_idx >= 0:
                vibe_buffer.append('</div>')
            vibe_buffer.append(f'<p>{inline_format(stripped)}</p>')
            i += 1
            continue

        # --- 空行 ---
        if not stripped:
            # flush 列表
            if in_list:
                if list_type == "ul":
                    html_parts.append(f'<ul>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ul>')
                else:
                    html_parts.append(f'<ol>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ol>')
                list_buffer = []
                in_list = False
                list_type = None
            i += 1
            continue

        # --- 表格 ---
        if "|" in stripped and stripped.startswith("|"):
            # 表格行
            table_rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                table_rows.append(lines[i])
                i += 1
            if table_rows:
                html_parts.append(convert_table(table_rows))
            continue

        # --- 标题 ---
        heading_match = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            h_text = heading_match.group(2).strip()
            # 跳过第一个 h2（已作为页面 h1 标题渲染）
            if level == 2 and not skipped_first_h2:
                skipped_first_h2 = True
                i += 1
                continue
            # ### → h2, #### → h3（body 内标题降一级）
            if skipped_first_h2 and level >= 3:
                level -= 1
            tag = f"h{level}"
            html_parts.append(f"<{tag}>{inline_format(h_text)}</{tag}>")
            i += 1
            continue

        # --- 引用块 ---
        if stripped.startswith(">"):
            if in_list:
                if list_type == "ul":
                    html_parts.append(f'<ul>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ul>')
                else:
                    html_parts.append(f'<ol>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ol>')
                list_buffer = []
                in_list = False
                list_type = None
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q = re.sub(r"^>\s*", "", lines[i].strip())
                quote_lines.append(q)
                i += 1
            if not any("vibe-prompt" in p for p in html_parts[-3:] if isinstance(p, str)):
                html_parts.append(f'<blockquote>')
                for q in quote_lines:
                    html_parts.append(f'<p>{inline_format(q)}</p>')
                html_parts.append(f'</blockquote>')
            continue

        # --- 列表 ---
        list_match = re.match(r"^(\s*)([-*]|\d+\.)\s+(.+)$", stripped)
        if list_match:
            indent = list_match.group(1)
            marker = list_match.group(2)
            content = list_match.group(3)

            if marker in ("-", "*"):
                current_type = "ul"
                li_content = content
            else:
                current_type = "ol"
                li_content = content

            if not in_list:
                in_list = True
                list_type = current_type
                list_buffer = []
            elif list_type != current_type:
                # 类型切换，flush 之前的列表
                if list_type == "ul":
                    html_parts.append(f'<ul>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ul>')
                else:
                    html_parts.append(f'<ol>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ol>')
                list_buffer = []
                list_type = current_type

            list_buffer.append(f'<li>{inline_format(li_content)}</li>')
            i += 1
            continue

        # --- 段落（普通文本或内联斜体）---
        if in_list:
            if list_type == "ul":
                html_parts.append(f'<ul>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ul>')
            else:
                html_parts.append(f'<ol>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ol>')
            list_buffer = []
            in_list = False
            list_type = None

        html_parts.append(f"<p>{inline_format(stripped)}</p>")
        i += 1

    # --- 清理收尾 ---
    if in_code_block:
        html_parts.append(f"<pre><code>{chr(10).join(code_buffer)}</code></pre>")

    if in_list:
        if list_type == "ul":
            html_parts.append(f'<ul>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ul>')
        else:
            html_parts.append(f'<ol>{chr(10)}{chr(10).join(list_buffer)}{chr(10)}</ol>')

    if in_takeaways:
        if any("<ul>" in l for l in takeaways_buffer) and not any("</ul>" in l for l in takeaways_buffer):
            takeaways_buffer.append("</ul>")
        html_parts.append(f'<div class="takeaways">{chr(10)}{chr(10).join(takeaways_buffer)}{chr(10)}</div>')

    if in_vibe:
        if any("vibe-prompt" in l for l in vibe_buffer) and not any("</div>" in l for l in vibe_buffer[-2:] if isinstance(l, str)):
            vibe_buffer.append("</div>")
        html_parts.append(render_vibe(vibe_buffer))

    if img_caption_pending:
        html_parts.append(f'<div class="img-caption">{inline_format(img_caption_pending)}</div>')

    # --- 组装 HTML ---
    body_content = "\n\n  ".join(html_parts)
    inline_style = generate_inline_style(theme)

    # 从目录名生成 chapter-meta（如 "02-生产关系的演变" → "第二章 · 生产关系的演变"）
    chapter_meta = ""
    meta_match = re.match(r"(\d+)-(.+)", rel_dir)
    if meta_match:
        num = meta_match.group(1)
        name = meta_match.group(2)
        cn_nums = {"01": "一", "02": "二", "03": "三", "04": "四", "05": "五", "06": "六",
                   "07": "七", "08": "八", "09": "九", "10": "十",
                   "11": "十一", "12": "十二", "13": "十三", "14": "十四", "15": "十五"}
        if num in cn_nums:
            chapter_meta = f"第{cn_nums[num]}章 · {name}"
        elif num == "16":
            chapter_meta = "附录"
    else:
        chapter_meta = rel_dir

    page_title = title if title else "章节"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link rel="stylesheet" href="../style.css">
<style>
  {inline_style}
</style>
</head>
<body>
<div class="container">
  <div class="chapter-meta">{chapter_meta}</div>
  <h1>{inline_format(page_title)}</h1>
  <div class="title-divider"></div>

  {body_content}

</div>
</body>
</html>"""

    return html


def convert_table(rows):
    """将 Markdown 表格行转换为 HTML 表格"""
    if len(rows) < 2:
        return ""

    # 第一行是表头
    header_cells = [c.strip() for c in rows[0].strip().split("|") if c.strip()]
    # 第二行是分隔符（跳过）
    # 后续行是数据行
    thead = "<thead><tr>"
    for h in header_cells:
        thead += f"<th>{inline_format(h)}</th>"
    thead += "</tr></thead>"

    tbody = "<tbody>"
    for row in rows[2:]:
        cells = [c.strip() for c in row.strip().split("|") if c.strip()]
        if cells:
            tbody += "<tr>"
            for c in cells:
                tbody += f"<td>{inline_format(c)}</td>"
            tbody += "</tr>"
    tbody += "</tbody>"

    return f'<table class="reading-path-table">{thead}{tbody}</table>'


def render_vibe(vibe_buffer):
    """渲染 Vibe 练习区块"""
    # 在前面插入 vibe-label
    vibeline = '\n  '.join(vibe_buffer)
    # 如果已经包含了 vibe-prompt 的开始，确保闭合
    has_prompt = any("vibe-prompt" in l for l in vibe_buffer)
    if has_prompt:
        if not any("</div>" in l for l in vibe_buffer[-2:] if isinstance(l, str)):
            vibeline += "\n</div>"
    return f'<div class="vibe-section">\n  <div class="vibe-label">Vibe 练习</div>\n  {vibeline}\n</div>'


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(BASE_DIR)

    total = 0

    for dirname in CHAPTER_DIRS:
        dir_path = os.path.join(BASE_DIR, dirname)
        if not os.path.isdir(dir_path):
            print(f"⚠  目录不存在: {dirname}")
            continue

        for fname in sorted(os.listdir(dir_path)):
            if not fname.endswith(".md"):
                continue
            md_path = os.path.join(dir_path, fname)
            html_fname = fname[:-3] + ".html"
            html_path = os.path.join(dir_path, html_fname)

            try:
                html_content = generate_html(md_path, dirname)
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(html_content)
                print(f"[OK] {dirname}/{html_fname}")
                total += 1
            except Exception as e:
                print(f"[ERR] {dirname}/{html_fname} - {e}")

    print(f"\nDone! Generated {total} HTML files.")


if __name__ == "__main__":
    main()
