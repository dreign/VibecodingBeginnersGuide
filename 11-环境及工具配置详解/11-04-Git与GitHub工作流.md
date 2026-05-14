<!--
  本节最后更新：2026-05-13
  验证环境：Git 2.x, GitHub
-->

## 11.4 Git 与 GitHub 工作流

### 一人公司也需要版本管理

很多人会觉得"我一个人做项目，不需要 Git"。但 Git 的价值不只是团队协作——它是一台**时间机器**。

- 改错了代码？可以回退到上一次提交的状态。
- 想尝试一个大改动又怕搞砸？开个分支随便试。
- 需要看看一周前写的某个功能是怎么实现的？Git 日志里翻一翻。

一人公司没有"有同事可以问"，Git 就是你的"同事"——它记得你做过的每一次修改。

**Git 对一人公司的三个核心价值：**

1. **安全网**。不知道这个改动会不会出问题？先 commit，然后放心大胆改。改坏了就 `git checkout .` 回到之前的版本。Git 让你敢于实验。
2. **历史记录**。一周后你可能会问自己"我当时为什么这么写？" Git log + commit message 会告诉你答案。如果你养成了写清楚 commit message 的习惯，Git 日志就是你的开发日记。
3. **远程备份**。把代码推到 GitHub/GitLab，等于多了一个异地备份。硬盘坏了不会丢代码。这是底线保障。

### 基本工作流

你只需要掌握几个命令就能工作：

```bash
# 初始化仓库
git init

# 查看当前状态（哪些文件改了、哪些还没 add）
git status

# 添加文件到暂存区
git add 文件名

# 添加所有改动的文件
git add .

# 提交修改
git commit -m "提交说明"

# 推送到 GitHub
git push
```

**典型的一次开发循环：**

```bash
# 开始工作前，确认仓库是干净的
git status

# 做你的修改——写代码、改代码

# 查看改了哪些文件
git status

# 查看具体改了哪些内容
git diff

# 把修改的文件添加到暂存区
git add 文件名1 文件名2

# 提交
git commit -m "添加用户登录页面的表单验证逻辑"

# 推送到远程
git push
```

这个循环你每天会跑很多次。不需要记住所有的 Git 命令——实际上在日常使用中，你主要用的就是 add、commit、push、status 这四个。

**常见的 Git 术语（不需要深入理解，知道存在就好）：**

- **仓库（repository）**：你的项目加上它的所有版本历史。
- **提交（commit）**：一次修改的快照。每个 commit 有唯一的 ID。
- **分支（branch）**：独立的开发线。默认叫 main 或 master。
- **暂存区（staging area）**：commit 之前的"缓冲区"。
- **远程（remote）**：存放在 GitHub 等服务器上的仓库副本。

### 分支策略：一人公司的简单方案

团队协作中分支管理很复杂——develop、feature、release、hotfix……对一人公司来说，你只需要一个最简单的策略：

**只用一个 main 分支，或者最多加一个 dev 分支。**

具体做法：

- **小改动、确定不会出问题的**：直接在 main 分支上改，改完 commit + push。
- **大改动、不确定的**：创建一个临时分支，改完后合并回 main。

创建和使用临时分支：

```bash
# 创建并切换到新分支
git checkout -b feature/new-login-page

# 在这个分支上做所有修改

# 改完之后，切回 main 分支
git checkout main

# 把新分支的改动合并进来
git merge feature/new-login-page

# 推送
git push

# 删除临时分支（已经合并完了，不需要了）
git branch -d feature/new-login-page
```

这个流程的关键好处：你的 main 分支始终是"可以运行的"——如果你有急事想部署，切回 main 就是上一个可用的版本。这个习惯会让你在一个人开发时多一层安全感。

### 让 AI 辅助写 commit message

如果你觉得写 commit message 很麻烦，让 AI 来做：

```
我已经修改了以下文件：
- src/components/Header.tsx
- src/pages/index.tsx
修改内容：将 Header 组件从深色主题改为浅色主题，并更新了首页的布局以适应新样式。
请帮我写一个简洁的 commit message。
```

AI 会返回类似这样的内容：

```
feat: 将 Header 组件切换为浅色主题并调整首页布局

- 更新 Header.tsx 中的主题变量和样式
- 调整 index.tsx 布局以适配新主题
- 确保深色/浅色切换时所有组件过渡平滑
```

你复制这个 commit message，用到 `git commit -m "..."` 中。

更省力的方式：让 AI 直接帮你生成并提交。

> "请帮我查看当前的 git diff，生成合适的 commit message，然后执行 git commit。"

AI 会自动运行 `git diff` 分析修改内容，生成 message，然后执行 commit。你只需要审查结果。

### 让 AI 辅助解决冲突

当你合并分支时，偶尔会遇到"冲突"——同一个文件的同一行在两个分支中被改成了不同的内容。Git 无法自动决定用哪个版本，需要你手动解决。

传统方式：打开冲突文件，找到 `<<<<<<<`、`=======`、`>>>>>>>` 标记，手动选择保留哪个版本的代码。

AI 辅助方式：

> "我在合并分支时遇到了冲突，帮我解决一下。保留两个版本中更完整的代码，如果有必要，把两者合并。"

AI 会读取冲突文件，分析两段代码的逻辑，帮你决定保留哪一段、或者如何合并两段。你确认后，AI 修改文件并执行 `git add`。

### .gitignore 的正确用法

`.gitignore` 告诉 Git "这些文件不要跟踪"。你需要它来保护敏感信息和避免将无关文件提交到仓库。

**必须忽略的：**
- `node_modules/`——npm 安装的依赖包，每个人运行 `npm install` 就能重新生成。一般占用几百 MB，不应该进版本管理。
- `.env` 或 `.env.local`——包含 API 密钥、数据库密码等敏感信息。如果这些被提交到公共 GitHub 仓库，相当于公开了你的密码。
- `dist/` 或 `.next/` 或 `build/`——构建产物，每次构建都会重新生成。

**建议忽略的：**
- `*.log`——日志文件，随时间增长且没有版本管理价值。
- `.DS_Store`——macOS 的文件系统元数据文件。
- `.vscode/` 或 `.idea/`——编辑器的个人配置文件（除非你和团队共用一套配置）。

让 AI 为你生成 .gitignore：

> "帮我创建一个适合 Next.js + TypeScript 项目的 .gitignore 文件，包含常见的需要忽略的目录和文件。"

AI 会生成一个完整的 .gitignore，直接写入你的项目根目录。

### GitHub：不只是代码托管

GitHub 不只是"放代码的地方"。即使你一个人开发，也可以利用 GitHub 的其他功能。

**GitHub Issues 作为个人任务管理。** 把你的开发计划写成 Issue：
- "添加用户注册功能"
- "修复移动端布局问题"
- "研究一下用什么支付方式"

每个 Issue 就是一个任务。完成一个关一个。比写在记事本上更系统，而且和你的代码仓库关联在一起。

**GitHub README 作为项目文档。** 在仓库根目录创建 README.md，记录项目是做什么的、怎么运行、有哪些功能。一个月后你回头看自己的项目，README 会让你快速记起当时的思路。

**GitHub Actions 做自动部署（进阶）。** 当你把代码推送到 GitHub 时，可以自动运行测试、构建、部署。这个在起步阶段不需要，但当你有了一个需要持续维护的项目后，它会节省你大量时间。

### 常见 Git 问题速查

**"我不小心在 main 分支上做了不应该做的修改怎么办？"**

如果还没 commit：`git checkout .` 撤销所有修改。如果已经 commit：`git revert HEAD` 创建一个"反 commit"来撤销上一次提交。或者用 Claude Code："我刚刚在 main 分支上做了一些改动，但本来应该在另一个分支上做。帮我恢复 main 到干净状态。"

**"我想撤销最近的一次 commit，但保留修改内容。"**

```bash
git reset --soft HEAD~1
```
这个命令撤销最近的 commit，保留修改文件在工作区中。你可以重新改、重新提交。

**"commit message 写错了怎么办？"**

```bash
git commit --amend -m "正确的提交说明"
```

**"我忘了 include 一个文件，想加到上一个 commit 里。"**

```bash
git add 忘记的文件
git commit --amend --no-edit
```

---

### 本节要点

- Git 对一人公司的价值是"时间机器"（回退版本）和"远程备份"（代码不丢），不只是团队协作工具。它让你敢于实验。
- 基本工作流只需 5 个命令：init、status、add、commit、push。日常循环：改代码 → add → commit → push。
- 分支策略：一人公司只需要 main 分支 + 临时 feature 分支。关键习惯——main 始终是可运行的版本。
- 让 AI 辅助 Git 操作：写 commit message、解决合并冲突、生成 .gitignore。减少你手动操作 Git 的频率。
- 底線操作：每次有意义的修改都提交、每天至少推送一次到 GitHub（远程备份）、敏感信息不进仓库（.gitignore）。
- GitHub 额外价值：Issues 做个人任务管理、README 做项目文档、Actions 做自动部署（进阶）。
- 常见问题：改错代码用 git checkout 或 git revert、commit 写错用 --amend、忘记 include 文件用 --amend --no-edit。

---

### Vibe 练习

在当前项目目录中运行：

> "请帮我初始化一个 Git 仓库，创建一个 .gitignore 文件（排除 node_modules、.env 等常见目录），然后帮我生成第一次提交的 commit message。"

进阶练习：

> 创建一个 Git 分支实验：让 AI "创建一个名为 experiment/new-ui 的分支，在这个分支上修改主页面的颜色主题（把蓝色改为绿色），然后提交。接着切回 main 分支，把 experiment 分支合并回来。" 观察 AI 如何完成 branch → checkout → commit → merge 的完整流程。