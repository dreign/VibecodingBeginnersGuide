<!--
  本节最后更新：2026-05-13
  验证环境：Claude Code v1.x, Windows/macOS
-->

## 11.2 Claude Code 安装与认证

### 安装 Claude Code

在确认 Node.js 已安装后，Claude Code 的安装只需要一行命令。

在终端中运行：

```bash
npm install -g @anthropic-ai/claude-code
```

`-g` 表示全局安装——安装后你在任何目录中都可以使用 `claude` 命令。如果不加 `-g`，它只会在当前目录下安装，你只能在当前目录中用 `npx claude` 运行。

安装完成后验证：

```bash
claude --version
```

如果显示了版本号，说明安装成功。

> **可能遇到的问题：**
> - **权限错误（EACCES）**：macOS/Linux 上可能出现。解决方式是在命令前加 `sudo`：`sudo npm install -g @anthropic-ai/claude-code`。
> - **npm 版本太旧**：如果安装过程报错，先升级 npm：`npm install -g npm@latest`。
> - **安装速度慢**：npm 默认使用国外的源。可以换成国内镜像：`npm config set registry https://registry.npmmirror.com`。安装完成后可以换回 `npm config set registry https://registry.npmjs.org`。
> - **Windows 上出现"禁止执行脚本"错误**：以管理员身份打开 PowerShell，运行 `Set-ExecutionPolicy RemoteSigned`。

### 更新 Claude Code

Claude Code 会频繁更新（几周一次），更新方式很简单：

```bash
npm update -g @anthropic-ai/claude-code
```

建议每个月检查一次更新。或者当你发现 Claude Code 的行为和本书描述不一致时，先更新到最新版试试。

查看当前版本和最新版本：

```bash
npm outdated -g @anthropic-ai/claude-code
```

如果输出显示 `Current` 和 `Wanted` 不一致，说明有新版本。

### 获取 API 密钥

Claude Code 通过 API 密钥来认证你的身份。获取 API 密钥的步骤：

1. 登录 https://console.anthropic.com
2. 在 API Keys 页面点击"Create Key"
3. 复制生成的密钥字符串（以 `sk-ant-` 开头）

**API 密钥不要泄露给他人**——把它想象成你的密码。不要把它上传到 GitHub、不要发在聊天群里、不要截图分享。如果有人拿到了你的密钥，他就可以用你的额度调用 API。

**关于 API 额度：**
- Anthropic 的 API 是付费的——按使用的 token 数量计费。
- 首次注册时会有一些免费额度（具体金额会变化，以官网为准），用完了需要绑定支付方式。
- 费用取决于你使用 Claude Code 的频率和任务复杂度。日常使用（每天几小时）每月费用通常在几十美元左右。
- 可以在 Anthropic Console 的 Billing 页面设置月度预算上限，防止意外超支。
- 你也可以在 Claude Code 中设置预算提醒：首次启动时工具会引导你配置。

> **省钱小技巧：**
> - 用 Claude Code 做"精确任务"比"漫无目的的对话"更省 token。每次对话前想清楚"我今天要做什么"。
> - 如果只需要简单问答或代码补全，IDE 插件（L2 工具）通常比 Claude Code 更便宜——它们使用的是轻量级模型或缓存机制。
> - 在 Claude Code 中可以用 `/compact` 命令让 AI 的回复更简洁，减少 token 消耗。

### 配置 API 密钥

有两种方式配置 API 密钥。

**方式一：环境变量（推荐）。**

在终端中设置：

```bash
# macOS / Linux
export ANTHROPIC_API_KEY=你的密钥

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="你的密钥"
```

每次打开新终端都需要重新设置，除非你把它添加到配置文件中。

让环境变量持久化（Windows）：
1. 打开"设置 → 系统 → 关于 → 高级系统设置 → 环境变量"
2. 在"用户变量"中点击"新建"
3. 变量名填 `ANTHROPIC_API_KEY`，变量值填你的密钥字符串
4. 确定后重启终端

让环境变量持久化（macOS/Linux）：
```bash
# 如果你用的是 zsh（macOS 默认）
echo 'export ANTHROPIC_API_KEY=你的密钥' >> ~/.zshrc

# 如果你用的是 bash
echo 'export ANTHROPIC_API_KEY=你的密钥' >> ~/.bashrc

# 重新加载配置文件
source ~/.zshrc  # 或 source ~/.bashrc
```

**方式二：在 Claude Code 首次运行时配置。**

如果你没有设置环境变量，首次运行 `claude` 时工具会提示你输入 API 密钥。输入后它会保存在本地配置文件中（通常位于 `~/.claude/claude_code.json` 或类似位置）。

这种方式更方便，但需要注意：如果你在多台电脑上使用 Claude Code，每台都需要单独配置。而环境变量的方式，如果你使用版本控制的配置文件，可以更统一地管理。

### 测试安装

在终端中运行：

```bash
claude
```

你会看到 Claude Code 启动，并进入对话模式。试着说一句最简单的指令：

> "你好，请确认我可以正常使用。"

如果 Claude Code 正常回复了，说明一切配置正确。按 Ctrl+C 退出对话。

**如果启动失败：**
- 检查 Node.js 是否安装：`node --version`
- 检查环境变量是否设置正确：`echo $ANTHROPIC_API_KEY`（macOS）或 `echo $env:ANTHROPIC_API_KEY`（Windows）
- 重新安装一次：先 `npm uninstall -g @anthropic-ai/claude-code`，再重新安装
- 如果仍然不行，在终端中查看错误信息——错误信息通常会告诉你问题出在哪里

### 配置选项

Claude Code 有一些可配置的选项，可以在启动后通过对话或配置文件调整。

**常用配置项：**

- **模型选择**：Claude Code 默认使用 Claude 的最新模型。如果你想使用特定版本，可以在對話中指定，比如"请使用 Claude Opus 模型处理这个任务"。
- **最大 token 数**：控制 AI 每次回复的最大长度。默认值通常够用，如果你在处理非常大的文件，可以调高。
- **上下文窗口**：Claude Code 可以看到你项目中的多少内容。如果需要更大的上下文（比如整个项目），可以调整。

这些配置项在起步阶段不需要改动。当你用了一段时间后，如果某个限制频繁遇到，再去找对应的配置。

### 多个项目中使用 Claude Code

Claude Code 是"项目感知"的——你在某个项目目录中启动 `claude`，它会把当前目录作为工作目录。你可以为不同项目准备不同的上下文和配置。

**常见做法：**
- 在项目 A 的目录下运行 `claude`，AI 自动以项目 A 为工作范围
- 切换到项目 B 时，按 Ctrl+C 退出，cd 到项目 B 目录，再运行 `claude`

Claude Code 没有"项目切换"命令——退出当前对话，在另一个目录中重新启动就行了。

---

### 本节要点

- 安装只需一行命令：`npm install -g @anthropic-ai/claude-code`。遇到权限错误用 sudo，安装慢换国内镜像。
- 需要 API 密钥来认证——在 Anthropic Console 创建。API 付费使用（首次有免费额度），建议设置预算上限。
- API 密钥配置推荐环境变量方式（设置 `ANTHROPIC_API_KEY`），也可以在首次运行时输入。
- 首次运行 `claude` 进入对话模式，验证安装是否成功。启动失败时检查 Node.js 版本、环境变量和错误信息。
- Claude Code 频繁更新，每月用 `npm update -g @anthropic-ai/claude-code` 检查更新。
- 多个项目中使用：在每个项目的目录下分别启动 claude。退出当前对话，cd 到另一个项目再启动。

---

### Vibe 练习

安装完成后，对 Claude Code 说：

> "帮我查看当前目录的结构，并告诉我这个目录是不是一个 Git 仓库。"

进阶练习：

> 对 Claude Code 说："请创建一个新的 Next.js 项目（使用 create-next-app），项目名为 my-test-project。完成后告诉我项目结构。" 观察 AI 如何在终端中一步步完成创建、安装依赖、初始化 Git 的完整流程。这个练习会帮你熟悉 Claude Code 的工作节奏。