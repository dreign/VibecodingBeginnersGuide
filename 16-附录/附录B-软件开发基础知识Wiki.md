<!--
  本节最后更新：2026-05-11
  验证环境：无（参考章节）
-->

## 附录 B 软件开发基础知识 Wiki

> 本节是为 Vibe Coding 读者准备的"最小必要知识"——不是大学计算机课程的精简版，而是你一个人做软件时需要知道的核心概念。

---

### B.1 计算机工作原理地图

从你写代码到程序运行，经过以下层次：

```
你写的代码（高级语言）
    ↓
编译/解释（变成机器指令）
    ↓
操作系统（管理资源分配）
    ↓
硬件（CPU → 内存 → 存储）
```

#### B.1.1 CPU（中央处理器）

电脑的"大脑"，执行指令。速度极快（每秒几十亿次运算），但一次只能做一件事。多任务是通过快速切换实现的。

**核心概念：**
- **指令周期**：取指令 → 解码 → 执行 → 写回
- **多核**：现代 CPU 通常有多个核心，可以真正并行执行
- **缓存**：CPU 内置高速缓存（L1、L2、L3），比内存快几十倍

#### B.1.2 内存（RAM）

短期记忆。程序和正在处理的数据放在这里。速度快，断电即消失。容量通常 8GB~32GB。

**核心概念：**
- **地址空间**：每个进程有独立的虚拟地址空间
- **分页**：内存被分成固定大小的页，便于管理
- **虚拟内存**：当物理内存不足时，操作系统会把部分内存内容写到硬盘（页面文件/交换分区）

#### B.1.3 存储（硬盘/SSD）

长期记忆。文件、安装的程序、操作系统放在这里。速度比内存慢 10~100 倍，但断电后数据不丢失。

**核心概念：**
- **HDD（硬盘驱动器）**：机械硬盘，靠磁头读写，速度较慢但容量大、价格低
- **SSD（固态硬盘）**：基于闪存，速度快、抗震，但价格较高
- **NVMe**：新一代 SSD 接口协议，比传统 SATA SSD 快数倍

#### B.1.4 I/O（输入/输出）

与外部世界的交互——键盘、鼠标、屏幕、网络、磁盘读写。

**核心概念：**
- **阻塞 I/O**：程序等待 I/O 完成后才能继续
- **非阻塞 I/O**：程序发起 I/O 后可以继续执行其他任务
- **DMA（直接内存访问）**：设备可以直接访问内存，不需要 CPU 干预

#### B.1.5 理解这些有什么实际用处

- **程序变慢了**：先检查内存是否满了（不够内存时会用硬盘做"虚拟内存"，速度骤降）
- **文件操作很慢**：不是程序差，是硬盘读写本来就比内存访问慢两个数量级
- **程序崩溃说"内存不足"**：你的程序占用的内存超过了电脑的物理内存
- **CPU 占用率高**：检查是否有死循环或计算密集型操作

---

### B.2 操作系统核心概念

#### B.2.1 文件系统

文件在硬盘上的组织方式。路径有绝对路径（`/home/user/project/`）和相对路径（`./src/index.js`）。

**常见文件系统：**
| 文件系统 | 特点 | 适用系统 |
|----------|------|---------|
| NTFS | 支持大文件、权限管理 | Windows |
| FAT32 | 兼容性好，单个文件最大 4GB | U盘、移动硬盘 |
| ext4 | 高性能、可靠性高 | Linux |
| APFS | 苹果文件系统，支持加密 | macOS |

**路径类型：**
- **绝对路径**：从根目录开始的完整路径，如 `/usr/local/bin/python`
- **相对路径**：相对于当前目录的路径，如 `../src/utils.js`
- **`.`**：当前目录
- **`..`**：父目录

#### B.2.2 进程与线程

**进程**：正在运行的程序实例。每个进程有独立的内存空间。进程之间默认不共享数据。

**线程**：进程内的执行单元。同一进程内的线程共享进程的内存空间，但有独立的执行栈。

**关键区别：**
| 特性 | 进程 | 线程 |
|------|------|------|
| 内存空间 | 独立 | 共享 |
| 创建开销 | 大 | 小 |
| 通信方式 | IPC（进程间通信） | 直接共享内存 |
| 隔离性 | 高 | 低 |

**进程状态：**
- **运行中**：正在 CPU 上执行
- **就绪**：等待 CPU 调度
- **阻塞**：等待 I/O 完成或其他事件
- **终止**：执行完毕

#### B.2.3 环境变量

操作系统级别的配置键值对。用于存储不随代码变化的配置：

```bash
# 设置（当前终端）
export DATABASE_URL="postgresql://localhost:5432/mydb"
export ANTHROPIC_API_KEY="sk-ant-xxx"

# 查看
echo $DATABASE_URL

# 查看所有环境变量
env

# 写入文件（持久化）
# Linux/macOS：添加到 ~/.bashrc 或 ~/.zshrc
# Windows：系统属性 -> 环境变量
```

**为什么环境变量重要：**
- API 密钥、数据库连接字符串、不同环境的配置——这些东西写在代码里是安全风险
- 环境变量是最安全的方式，不会被提交到版本控制
- 方便在不同环境（开发、测试、生产）使用不同配置

#### B.2.4 标准流

每个进程有三个默认通道：

| 流 | 名称 | 用途 | 文件描述符 |
|----|------|------|-----------|
| stdin | 标准输入 | 键盘输入 | 0 |
| stdout | 标准输出 | 正常输出（屏幕） | 1 |
| stderr | 标准错误 | 错误信息 | 2 |

**重定向：**
```bash
# 将 stdout 重定向到文件（覆盖）
node app.js > output.log

# 将 stdout 追加到文件
node app.js >> output.log

# 将 stderr 重定向到文件
node app.js 2> error.log

# 将 stdout 和 stderr 都重定向到同一文件
node app.js > combined.log 2>&1

# 丢弃输出（黑洞）
node app.js > /dev/null 2>&1
```

#### B.2.5 退出码

程序正常退出返回 `0`，出错返回非零值。Shell 脚本中常用 `$?` 获取上一个命令的退出码。

```bash
# 运行命令
node app.js

# 检查退出码
if [ $? -eq 0 ]; then
  echo "成功"
else
  echo "失败"
fi
```

**常见退出码：**
| 退出码 | 含义 |
|--------|------|
| 0 | 成功 |
| 1 | 通用错误 |
| 2 | 用法错误 |
| 127 | 命令未找到 |
| 128 | 无效参数 |
| 128+n | 收到信号 n 而终止 |

#### B.2.6 信号处理

操作系统通过信号与进程通信。常见信号：

| 信号 | 名称 | 含义 | 默认行为 |
|------|------|------|---------|
| SIGINT (2) | 中断 | 用户按 Ctrl+C | 终止 |
| SIGTERM (15) | 终止 | 请求优雅关闭 | 终止 |
| SIGKILL (9) | 杀死 | 强制终止（无法捕获） | 终止 |
| SIGQUIT (3) | 退出 | 用户按 Ctrl+\ | 终止并转储核心 |
| SIGHUP (1) | 挂起 | 终端关闭 | 终止 |

```bash
# 发送信号
kill -TERM <PID>    # 优雅终止
kill -KILL <PID>    # 强制终止
kill -INT <PID>     # 模拟 Ctrl+C

# 捕获信号（Node.js 示例）
process.on('SIGTERM', () => {
  console.log('收到 SIGTERM，正在优雅关闭...');
  server.close(() => {
    process.exit(0);
  });
});
```

#### B.2.7 进程间通信（IPC）

进程之间交换数据的方式：

| 方式 | 描述 | 适用场景 |
|------|------|---------|
| 管道 (Pipe) | 单向数据流 | 父子进程通信 |
| 命名管道 (FIFO) | 双向命名管道 | 无亲缘关系进程 |
| 信号 | 简单通知 | 事件通知 |
| 共享内存 | 内存区域共享 | 高性能数据共享 |
| 消息队列 | 消息传递 | 异步通信 |
| Socket | 网络通信 | 跨机器通信 |

```bash
# 管道示例
ls -la | grep ".txt"  # 将 ls 输出传给 grep

# 命名管道
mkfifo mypipe
cat < mypipe &        # 后台读取
echo "hello" > mypipe # 写入
```

---

### B.3 网络基础

#### B.3.1 IP 地址

互联网上的"门牌号"。IPv4 格式如 `192.168.1.1`，IPv6 格式如 `2001:db8::1`。

**IP 地址分类：**
- **公网 IP**：全球唯一，直接连上互联网的设备有
- **内网 IP**：局域网内使用（如 `192.168.x.x`、`10.x.x.x`、`172.16.x.x-172.31.x.x`），通过路由器转换
- **127.0.0.1（localhost）**：指向本机，开发时常用

**NAT（网络地址转换）：**
- 路由器将内网 IP 转换为公网 IP
- 多个设备共享一个公网 IP
- 端口映射：将路由器端口映射到内网设备

#### B.3.2 DNS（域名系统）

把 `google.com` 这样的域名翻译成 IP 地址。类似电话本。

**DNS 查询过程：**
1. 浏览器检查本地缓存
2. 查询本地 DNS 服务器
3. 递归查询根域名服务器 → 顶级域名服务器 → 权威域名服务器

**常见 DNS 记录：**
| 记录类型 | 用途 |
|----------|------|
| A | 域名 → IPv4 地址 |
| AAAA | 域名 → IPv6 地址 |
| CNAME | 域名别名 |
| MX | 邮件服务器 |
| TXT | 文本记录（常用于验证） |

```bash
# 查询 DNS 记录
dig google.com
nslookup example.com

# 刷新 DNS 缓存（macOS）
dscacheutil -flushcache

# 刷新 DNS 缓存（Windows）
ipconfig /flushdns
```

#### B.3.3 HTTP/HTTPS

浏览器和服务器之间的通信协议。HTTPS = HTTP + 加密（SSL/TLS）。

**HTTP 特点：**
- 无状态：每个请求独立，服务器不保留会话信息
- 明文传输：数据以明文发送，不安全
- 端口：80

**HTTPS 特点：**
- 加密传输：数据通过 SSL/TLS 加密
- 证书验证：验证服务器身份
- 端口：443

**TLS 握手过程：**
1. 客户端发送支持的加密套件
2. 服务器返回证书
3. 客户端验证证书
4. 协商对称密钥
5. 加密通信

#### B.3.4 常见的 HTTP 方法

| 方法 | 含义 | 幂等性 | 常用场景 |
|------|------|--------|---------|
| GET | 获取数据 | 是 | 查看资源 |
| POST | 创建数据 | 否 | 提交表单、创建资源 |
| PUT | 更新数据 | 是 | 替换资源 |
| PATCH | 部分更新 | 否 | 更新资源的部分字段 |
| DELETE | 删除数据 | 是 | 删除资源 |
| HEAD | 获取响应头 | 是 | 检查资源是否存在 |
| OPTIONS | 获取服务器支持的方法 | 是 | CORS 预检请求 |

**幂等性**：多次调用产生相同的效果

#### B.3.5 HTTP 状态码

| 状态码 | 类别 | 含义 |
|--------|------|------|
| 1xx | 信息性 | 请求已接收，继续处理 |
| 2xx | 成功 | 请求成功处理 |
| 3xx | 重定向 | 需要进一步操作 |
| 4xx | 客户端错误 | 请求有问题 |
| 5xx | 服务器错误 | 服务器处理失败 |

**常见状态码：**
| 状态码 | 含义 |
|--------|------|
| 200 | OK（成功） |
| 201 | Created（创建成功） |
| 204 | No Content（无内容） |
| 301 | Moved Permanently（永久重定向） |
| 302 | Found（临时重定向） |
| 400 | Bad Request（请求错误） |
| 401 | Unauthorized（未授权） |
| 403 | Forbidden（禁止访问） |
| 404 | Not Found（未找到） |
| 500 | Internal Server Error（服务器错误） |
| 503 | Service Unavailable（服务不可用） |

#### B.3.6 端口

一台服务器上可以运行多个网络服务，通过端口号区分。端口范围：0~65535。

**知名端口（0~1023）：**
| 端口 | 服务 |
|------|------|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

**注册端口（1024~49151）：**
| 端口 | 服务 |
|------|------|
| 3000 | Next.js / React 开发服务器 |
| 5000 | Flask / FastAPI 开发服务器 |
| 8080 | HTTP 替代端口 |
| 8000 | Django 开发服务器 |

**动态端口（49152~65535）：**
- 客户端使用的临时端口

#### B.3.7 WebSocket

HTTP 只能由"客户端请求、服务器响应"。WebSocket 允许服务器主动向客户端推送数据——适合聊天、实时通知、实时数据更新。

**WebSocket 特点：**
- 双向通信
- 持久连接
- 低延迟
- 基于 TCP

**WebSocket 握手：**
```
客户端 → 服务器：HTTP 请求（包含 Upgrade: websocket）
服务器 → 客户端：101 Switching Protocols
```

**适用场景：**
- 实时聊天应用
- 实时数据更新（股票、体育比分）
- 多人协作工具
- 在线游戏

#### B.3.8 TCP/IP 协议栈

网络通信的层次模型：

| 层次 | 协议 | 功能 |
|------|------|------|
| 应用层 | HTTP, HTTPS, FTP, DNS | 用户交互 |
| 传输层 | TCP, UDP | 端到端通信 |
| 网络层 | IP, ICMP, ARP | 路由和寻址 |
| 链路层 | Ethernet, Wi-Fi | 物理介质传输 |

**TCP 三次握手：**
```
客户端 → 服务器：SYN（请求建立连接）
服务器 → 客户端：SYN + ACK（确认收到，同意建立）
客户端 → 服务器：ACK（确认，连接建立）
```

**TCP 四次挥手：**
```
客户端 → 服务器：FIN（请求关闭）
服务器 → 客户端：ACK（确认收到）
服务器 → 客户端：FIN（准备关闭）
客户端 → 服务器：ACK（确认，连接关闭）
```

**UDP vs TCP：**
| 特性 | TCP | UDP |
|------|-----|-----|
| 可靠性 | 可靠（重传机制） | 不可靠 |
| 连接 | 面向连接 | 无连接 |
| 速度 | 较慢 | 较快 |
| 适用场景 | 文件传输、网页、API | 视频通话、游戏、流媒体 |

#### B.3.9 CDN（内容分发网络）

将静态资源分发到全球边缘节点，降低延迟。

**CDN 工作原理：**
1. 用户请求资源
2. DNS 解析到最近的边缘节点
3. 边缘节点返回缓存的资源
4. 若未缓存，向源站请求并缓存

**CDN 配置示例：**
```javascript
// Cloudflare CDN 配置（next.config.js）
module.exports = {
  images: {
    domains: ['example.com'],
    loader: 'cloudflare',
    path: '/cdn-cgi/image/',
  },
};
```

---

### B.4 数据格式

#### B.4.1 JSON

Web 应用中最通用的数据格式。

```json
{
  "name": "Alice",
  "age": 30,
  "isActive": true,
  "skills": ["JavaScript", "Python"],
  "address": {
    "city": "Beijing",
    "zip": "100000"
  },
  "tags": null
}
```

**JSON 语法规则：**
- 键名必须用双引号
- 字符串必须用双引号
- 支持的类型：string、number、boolean、null、array、object
- 最后一个元素后不能有逗号

**JSON 与 JavaScript 对象的区别：**
- JSON 是纯文本格式
- JSON 键名必须用双引号
- JSON 不支持 undefined、function、Date 对象
- JSON 数字不能有前导零

**JSON 操作（JavaScript）：**
```javascript
// 对象 → JSON 字符串
const data = { name: "Alice", age: 30 };
const jsonStr = JSON.stringify(data);

// JSON 字符串 → 对象
const parsed = JSON.parse(jsonStr);

// 格式化输出
const pretty = JSON.stringify(data, null, 2);
```

**JSON 操作（Python）：**
```python
import json

# 对象 → JSON 字符串
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data, indent=2)

# JSON 字符串 → 对象
parsed = json.loads(json_str)

# 读取文件
with open("data.json", "r") as f:
    data = json.load(f)

# 写入文件
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

#### B.4.2 YAML

比 JSON"更可读"的配置格式。用缩进表示层级，支持注释。

```yaml
# 配置示例
server:
  host: "0.0.0.0"
  port: 3000
  timeout: 30
  debug: false

database:
  url: "postgresql://localhost:5432/mydb"
  username: "admin"
  password: "secret"
  options:
    pool_size: 20
    max_overflow: 5

logging:
  level: "info"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  handlers:
    - console
    - file

features:
  enable_notifications: true
  enable_analytics: false
  api_keys:
    - "key1"
    - "key2"
    - "key3"
```

**YAML 语法规则：**
- 使用空格缩进（不要用 Tab）
- 键值对用冒号分隔，冒号后要有空格
- 列表用 `- ` 开头
- 支持多行字符串（`|` 和 `>`）
- 支持注释（`#`）

**YAML 数据类型：**
```yaml
# 字符串
name: "Alice"
name2: Alice  # 简单字符串可以不加引号

# 数字
count: 42
price: 3.14
big_number: 1e10

# 布尔值
is_active: true
is_deleted: false

# 空值
empty: null
empty2: ~

# 日期时间
date: 2024-01-15
datetime: 2024-01-15T10:30:00Z

# 列表
fruits:
  - apple
  - banana
  - cherry

# 嵌套对象
user:
  name: "Alice"
  age: 30
  address:
    city: "Beijing"
```

#### B.4.3 Markdown

本书使用的格式。简单的标记语法：

```markdown
# 一级标题
## 二级标题
### 三级标题

**粗体文本**
*斜体文本*
~~删除线~~

- 无序列表项 1
- 无序列表项 2
  - 嵌套列表项
  - 嵌套列表项

1. 有序列表项 1
2. 有序列表项 2
3. 有序列表项 3

[链接文本](https://example.com)
![图片替代文本](image.jpg)

> 引用文本
>> 嵌套引用

`行内代码`

```javascript
// 代码块
function hello() {
  console.log("Hello World");
}
```

| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 值1 | 值2 | 值3 |
| 值4 | 值5 | 值6 |

---

脚注[^1]

[^1]: 这是脚注内容
```

**Markdown 扩展语法（GitHub Flavored Markdown）：**
```markdown
- [x] 已完成任务
- [ ] 未完成任务

~~删除线文本~~

| 左对齐 | 居中 | 右对齐 |
|:-------|:----:|-------:|
| 内容 | 内容 | 内容 |

> [!NOTE]
> 注意信息

> [!WARNING]
> 警告信息

\*转义星号\*
```

#### B.4.4 CSV（逗号分隔值）

简单的表格数据格式，广泛用于数据交换。

```csv
name,age,city,email
Alice,30,Beijing,alice@example.com
Bob,25,Shanghai,bob@example.com
Charlie,35,Guangzhou,charlie@example.com
```

**CSV 语法规则：**
- 第一行通常是表头
- 字段用逗号分隔
- 包含逗号、引号或换行的字段需要用引号包围
- 引号内的引号需要转义（用两个引号）

**CSV 操作（Python）：**
```python
import csv

# 读取 CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# 写入 CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'Beijing'])
```

#### B.4.5 XML（可扩展标记语言）

结构化数据格式，曾广泛用于配置和数据交换。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<users>
  <user id="1">
    <name>Alice</name>
    <age>30</age>
    <city>Beijing</city>
    <active>true</active>
  </user>
  <user id="2">
    <name>Bob</name>
    <age>25</age>
    <city>Shanghai</city>
    <active>false</active>
  </user>
</users>
```

**XML 与 JSON 对比：**
| 特性 | XML | JSON |
|------|-----|------|
| 可读性 | 较复杂 | 简洁 |
| 大小 | 较大 | 较小 |
| 解析速度 | 较慢 | 较快 |
| 支持注释 | 是 | 否 |
| 属性支持 | 是 | 否 |

#### B.4.6 Protobuf（Protocol Buffers）

Google 开发的高效序列化格式，适合高性能数据传输。

```protobuf
// user.proto
syntax = "proto3";

message User {
  string name = 1;
  int32 age = 2;
  string city = 3;
  bool is_active = 4;
  repeated string skills = 5;
}
```

**Protobuf 特点：**
- 二进制格式，体积小
- 解析速度快
- 支持版本兼容
- 需要编译工具

---

### B.5 安全常识

#### B.5.1 API 密钥保护

**最佳实践：**

| 做法 | 是否推荐 | 说明 |
|------|---------|------|
| ❌ 写在代码里 | 否 | 会被提交到 Git 仓库 |
| ✅ 使用环境变量 | 是 | 安全且不进入版本控制 |
| ❌ 在聊天或邮件中发送 | 否 | 容易泄露 |
| ✅ 密钥泄露后立即吊销 | 是 | 在服务商控制台操作 |
| ❌ 多个服务共用密钥 | 否 | 一个泄露全部受影响 |
| ✅ 使用 `.env` 文件 | 是 | 确保在 `.gitignore` 中 |
| ✅ 定期轮换密钥 | 是 | 降低泄露风险 |
| ❌ 硬编码在客户端代码中 | 否 | 可被轻易提取 |

**.gitignore 示例：**
```
# 环境变量文件
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# 日志文件
*.log
npm-debug.log*
yarn-debug.log*

# 依赖目录
node_modules/
__pycache__/
```

#### B.5.2 CORS（跨域资源共享）

浏览器安全机制——默认不允许一个域名下的网页访问另一个域名下的 API。

**CORS 响应头：**
| 响应头 | 作用 |
|--------|------|
| Access-Control-Allow-Origin | 指定允许的源（`*` 表示所有） |
| Access-Control-Allow-Methods | 指定允许的 HTTP 方法 |
| Access-Control-Allow-Headers | 指定允许的请求头 |
| Access-Control-Allow-Credentials | 是否允许携带凭证 |
| Access-Control-Max-Age | 预检请求的缓存时间 |

**CORS 预检请求（OPTIONS）：**
- 当请求不是简单请求时，浏览器会先发送 OPTIONS 请求
- 检查服务器是否允许该请求
- 缓存预检结果以提高性能

**常见 CORS 配置（Express.js）：**
```javascript
const express = require('express');
const cors = require('cors');

const app = express();

// 允许所有来源（开发环境）
app.use(cors());

// 允许指定来源
app.use(cors({
  origin: 'https://example.com',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true
}));
```

**常见 CORS 配置（FastAPI）：**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### B.5.3 XSS（跨站脚本攻击）

攻击者把恶意脚本注入到你的网站中。

**XSS 类型：**
| 类型 | 描述 |
|------|------|
| 存储型 | 恶意脚本存储在服务器（如评论、帖子） |
| 反射型 | 恶意脚本在 URL 中，服务器直接返回 |
| DOM 型 | 恶意脚本通过客户端 JavaScript 执行 |

**防御方案：**
1. **永远不要直接把用户输入插入到 HTML 中**
2. 使用框架提供的安全机制（React、Vue 等默认转义）
3. 对用户输入进行验证和清理
4. 使用 `textContent` 而非 `innerHTML`
5. 配置 CSP（内容安全策略）

**CSP 示例：**
```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' 'unsafe-eval';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data:;
">
```

#### B.5.4 CSRF（跨站请求伪造）

攻击者诱导用户在已登录的状态下执行非本意的操作。

**防御方案：**
1. **CSRF Token**：在表单中加入随机 token
2. **Same-Site Cookie 属性**：限制 Cookie 发送范围
3. **验证 Referer 头**：检查请求来源
4. **双重提交 Cookie**：将 CSRF token 放在 Cookie 和请求体中

**CSRF Token 示例：**
```html
<form action="/submit" method="POST">
  <input type="hidden" name="csrf_token" value="random-token">
  <input type="text" name="content">
  <button type="submit">提交</button>
</form>
```

#### B.5.5 SQL 注入

攻击者通过输入恶意 SQL 语句来操作数据库。

**危险示例：**
```javascript
// 直接拼接用户输入（危险！）
const username = req.body.username;
const query = `SELECT * FROM users WHERE username = '${username}'`;
// 如果 username 是 ' OR '1'='1，则会变成：
// SELECT * FROM users WHERE username = '' OR '1'='1'
// 这会返回所有用户！
```

**防御方案：**
1. **使用参数化查询**（Prepared Statements）
2. **使用 ORM**（如 Prisma、SQLAlchemy）
3. **对用户输入进行验证**
4. **最小权限原则**：数据库用户只授予必要权限

**安全示例（参数化查询）：**
```javascript
// 使用参数化查询
const username = req.body.username;
const query = 'SELECT * FROM users WHERE username = ?';
db.query(query, [username], (err, results) => {
  // 处理结果
});
```

#### B.5.6 HTTPS 强制

生产环境必须使用 HTTPS——浏览器会标记非 HTTPS 网站为"不安全"。

**HTTPS 证书获取：**
- **Let's Encrypt**：免费证书
- **Cloudflare**：提供免费 SSL
- **商业证书**：购买证书

**HTTPS 配置：**
- Vercel、Netlify、GitHub Pages 默认提供 HTTPS
- 自托管服务需要配置 SSL 证书
- 配置 HTTP → HTTPS 重定向

#### B.5.7 密码安全

**密码存储最佳实践：**
- 永远不要明文存储密码
- 使用强哈希算法（bcrypt、Argon2）
- 添加随机盐值
- 定期轮换密码

**密码哈希示例（Node.js）：**
```javascript
const bcrypt = require('bcrypt');
const saltRounds = 12;

// 哈希密码
async function hashPassword(password) {
  return bcrypt.hash(password, saltRounds);
}

// 验证密码
async function verifyPassword(password, hash) {
  return bcrypt.compare(password, hash);
}
```

**密码哈希示例（Python）：**
```python
import bcrypt

# 哈希密码
password = b"my_password"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

# 验证密码
bcrypt.checkpw(password, hashed)  # True
```

**密码策略：**
| 规则 | 建议 |
|------|------|
| 最小长度 | 12-16 位 |
| 复杂度 | 混合大小写、数字、特殊字符 |
| 过期时间 | 90-180 天 |
| 历史记录 | 禁止使用最近 3-5 个密码 |
| 重试限制 | 5 次失败后锁定账户 |

#### B.5.8 会话管理

**会话安全最佳实践：**

| 措施 | 说明 |
|------|------|
| 使用 HttpOnly Cookie | 防止 XSS 获取会话 ID |
| 使用 Secure Cookie | 只通过 HTTPS 传输 |
| 设置 SameSite 属性 | 防止 CSRF |
| 设置合理过期时间 | 短期会话更安全 |
| 定期轮换会话 ID | 登录成功后重新生成 |
| 注销时清除会话 | 服务器端和客户端都清除 |

**Cookie 配置示例：**
```javascript
res.cookie('sessionId', sessionId, {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'strict',
  maxAge: 24 * 60 * 60 * 1000, // 24小时
  path: '/'
});
```

#### B.5.9 安全审计清单

| 检查项 | 说明 |
|--------|------|
| 输入验证 | 所有用户输入都经过验证和清理 |
| 输出编码 | 动态内容正确转义 |
| 身份认证 | 使用强密码策略和多因素认证 |
| 授权控制 | 最小权限原则，验证权限 |
| 敏感数据 | 使用环境变量存储密钥 |
| 日志监控 | 记录安全事件，定期审查 |
| 依赖检查 | 定期更新依赖，检查漏洞 |
| 备份恢复 | 定期备份，测试恢复流程 |

---

### B.6 软件许可与合规

#### B.6.1 开源许可证速查

| 许可证 | 允许商用 | 要求开源 | 说明 |
|--------|---------|---------|------|
| MIT | ✅ | ❌ | 最宽松，几乎无限制 |
| Apache 2.0 | ✅ | ❌ | MIT 基础上增加了专利保护 |
| GPL v3 | ✅ | ✅ | 使用 GPL 代码的项目必须也使用 GPL |
| GPL v2 | ✅ | ✅ | 比 GPL v3 限制稍宽松 |
| LGPL | ✅ | 部分 | 库可以商用，但修改的库代码需开源 |
| BSD 2-Clause | ✅ | ❌ | 简单宽松，保留版权声明 |
| BSD 3-Clause | ✅ | ❌ | 比 2-Clause 多了广告限制 |
| MPL | ✅ | 部分 | Mozilla 公共许可证 |

**许可证选择建议：**
- **库/工具**：MIT 或 Apache 2.0（宽松，鼓励使用）
- **应用程序**：根据需求选择，MIT 最灵活
- **需要强制开源**：GPL
- **嵌入到专有软件**：LGPL 或 MIT

#### B.6.2 AI 生成代码的版权问题

截至 2026 年，各国对 AI 生成内容的版权尚无统一法律定论。实际建议：

| 使用场景 | 风险评估 | 建议 |
|----------|---------|------|
| 个人项目 | 低 | 基本不需要担心 |
| 开源项目 | 中 | 在 LICENSE 中说明使用了 AI |
| 商业产品 | 中 | 避免直接复制，进行修改 |
| 直接复制 GPL 代码 | 高 | 有潜在风险 |
| 通用代码（CRUD、UI组件） | 低 | 通常不涉及版权问题 |

**最佳实践：**
1. **避免让 AI 重写现有库**——这明显是越过许可使用
2. **对 AI 生成的代码进行审查和修改**——加入自己的理解
3. **保留修改记录**——证明是自己的工作
4. **使用 AI 作为辅助工具**——而非直接复制粘贴

#### B.6.3 隐私合规

**GDPR（欧盟通用数据保护条例）：**
- 用户有权访问、更正、删除其个人数据
- 需要明确的同意机制
- 数据泄露需在 72 小时内报告

**CCPA（加州消费者隐私法案）：**
- 用户有权知道收集了哪些数据
- 用户有权要求删除数据
- 禁止出售用户数据（除非用户明确同意）

**数据处理原则：**
| 原则 | 说明 |
|------|------|
| 合法、公平、透明 | 处理数据必须合法，用户知情 |
| 目的限制 | 只收集实现特定目的所需的数据 |
| 数据最小化 | 收集的数据量不超过必要 |
| 准确性 | 保持数据准确及时更新 |
| 存储限制 | 只在需要的时间内存储 |
| 完整性和保密性 | 保护数据安全 |

**隐私政策要点：**
- 收集哪些数据
- 为什么收集这些数据
- 数据如何使用
- 数据存储时间
- 用户权利

---

### B.7 容器与虚拟化

#### B.7.1 容器基础概念

**容器 vs 虚拟机：**

| 特性 | 容器 | 虚拟机 |
|------|------|--------|
| 隔离方式 | 操作系统级隔离 | 硬件级隔离 |
| 资源开销 | 低（共享内核） | 高（完整操作系统） |
| 启动速度 | 秒级 | 分钟级 |
| 镜像大小 | 小（通常 MB 级） | 大（通常 GB 级） |
| 移植性 | 高 | 较低 |

**容器核心组件：**

1. **容器引擎**：负责运行和管理容器（如 Docker Engine）
2. **容器镜像**：只读模板，包含应用程序及其依赖
3. **容器运行时**：执行容器的环境（如 runc）
4. **容器编排**：管理大规模容器部署（如 Kubernetes）

#### B.7.2 Docker 核心概念

**Dockerfile 最佳实践：**

```dockerfile
# 使用多阶段构建减少镜像大小
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

**Docker 网络模式：**

| 模式 | 描述 |
|------|------|
| `bridge` | 默认模式，容器之间通过虚拟网桥通信 |
| `host` | 容器共享宿主机网络栈 |
| `none` | 容器无网络连接 |
| `container:<name>` | 共享另一个容器的网络命名空间 |

**Docker 存储：**

| 类型 | 描述 |
|------|------|
| 卷（Volume） | 持久化存储，由 Docker 管理 |
| 绑定挂载（Bind Mount） | 挂载宿主机文件或目录 |
| tmpfs | 临时文件系统，容器退出后数据丢失 |

#### B.7.3 Kubernetes 基础

**核心组件：**

| 组件 | 描述 |
|------|------|
| Pod | 最小部署单元，可包含一个或多个容器 |
| Service | 为 Pod 提供稳定的网络访问 |
| Deployment | 管理 Pod 的部署和更新 |
| ReplicaSet | 确保指定数量的 Pod 副本运行 |
| ConfigMap | 存储配置数据 |
| Secret | 存储敏感数据（base64 编码） |
| Volume | 持久化存储 |

**Pod 配置示例：**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  containers:
    - name: web
      image: my-app:latest
      ports:
        - containerPort: 3000
      env:
        - name: NODE_ENV
          value: "production"
      resources:
        requests:
          memory: "128Mi"
          cpu: "100m"
        limits:
          memory: "256Mi"
          cpu: "200m"
      volumeMounts:
        - name: data
          mountPath: /app/data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: my-pvc
```

**Service 配置示例：**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  type: ClusterIP
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
```

---

### B.8 CI/CD 基础

#### B.8.1 CI/CD 概念

**CI（持续集成）：**
- 频繁将代码合并到主分支
- 自动构建和测试
- 快速发现集成问题

**CD（持续交付）：**
- 代码随时可部署到生产环境
- 自动化测试和验证
- 手动触发部署

**CD（持续部署）：**
- 代码自动部署到生产环境
- 无需人工干预

#### B.8.2 GitHub Actions 示例

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
      - name: Run lint
        run: npm run lint

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: build
          path: dist/
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

#### B.8.3 GitLab CI 示例

```yaml
stages:
  - test
  - build
  - deploy

test:
  stage: test
  image: node:18
  script:
    - npm ci
    - npm test
    - npm run lint

build:
  stage: build
  image: node:18
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

deploy:
  stage: deploy
  image: alpine
  script:
    - apk add --no-cache curl
    - curl -X POST https://api.vercel.com/v1/integrations/deploy/prj_xxx/${{ secrets.VERCEL_TOKEN }}
  only:
    - main
```

---

### B.9 监控与日志

#### B.9.1 监控指标

**关键指标类型：**

| 类型 | 描述 | 示例 |
|------|------|------|
| 基础设施指标 | CPU、内存、磁盘、网络 | CPU 使用率、内存占用 |
| 应用指标 | 请求数、响应时间、错误率 | QPS、P95 响应时间 |
| 业务指标 | 用户数、转化率、收入 | 日活用户、订单数 |

**常用监控工具：**

| 工具 | 用途 |
|------|------|
| Prometheus | 开源监控系统 |
| Grafana | 可视化仪表盘 |
| Datadog | 云原生监控 |
| New Relic | 全栈监控 |

**Prometheus 指标类型：**

```yaml
# Counter - 递增计数器
http_requests_total{method="GET", endpoint="/api/users"} 12345

# Gauge - 瞬时值
cpu_usage{core="0"} 42.5

# Histogram - 直方图
http_request_duration_seconds_bucket{le="0.1"} 100
http_request_duration_seconds_bucket{le="0.5"} 200
http_request_duration_seconds_sum 150.5
http_request_duration_seconds_count 250

# Summary - 摘要
http_request_duration_seconds{quantile="0.5"} 0.2
http_request_duration_seconds{quantile="0.95"} 0.8
```

#### B.9.2 日志管理

**日志级别：**

| 级别 | 描述 | 使用场景 |
|------|------|---------|
| DEBUG | 详细调试信息 | 开发阶段调试 |
| INFO | 一般信息 | 正常运行状态 |
| WARN | 警告信息 | 潜在问题 |
| ERROR | 错误信息 | 可恢复的错误 |
| FATAL | 致命错误 | 程序崩溃 |

**日志最佳实践：**

```javascript
// 结构化日志
const logger = {
  info: (message, context = {}) => {
    console.log(JSON.stringify({
      level: 'INFO',
      timestamp: new Date().toISOString(),
      message,
      ...context
    }));
  },
  error: (message, error, context = {}) => {
    console.error(JSON.stringify({
      level: 'ERROR',
      timestamp: new Date().toISOString(),
      message,
      error: {
        name: error.name,
        message: error.message,
        stack: error.stack
      },
      ...context
    }));
  }
};

// 使用示例
logger.info('User logged in', { userId: 123, ip: '192.168.1.1' });
logger.error('Failed to fetch user', new Error('Network error'), { userId: 123 });
```

**日志收集工具：**

| 工具 | 用途 |
|------|------|
| ELK Stack | Elasticsearch、Logstash、Kibana |
| Loki | Grafana 生态日志系统 |
| Datadog Logs | 云原生日志管理 |
| Splunk | 企业级日志分析 |

---

### B.10 性能优化

#### B.10.1 前端性能优化

**加载优化：**

| 技术 | 描述 |
|------|------|
| 代码分割 | 将代码拆分成小块，按需加载 |
| 懒加载 | 延迟加载非关键资源 |
| 缓存策略 | 使用 HTTP 缓存和 Service Worker |
| 图片优化 | 使用 WebP/AVIF 格式，响应式图片 |
| 压缩 | Gzip/Brotli 压缩 |

**运行时优化：**

| 技术 | 描述 |
|------|------|
| 虚拟列表 | 只渲染可见区域 |
| 防抖节流 | 减少频繁操作 |
| Web Workers | 后台处理耗时任务 |
| 内存管理 | 及时清理不再使用的引用 |

**代码示例：**

```javascript
// 防抖
function debounce(fn, delay = 300) {
  let timer = null;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// 节流
function throttle(fn, limit = 100) {
  let inThrottle = false;
  return function(...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// 虚拟列表（简化版）
class VirtualList {
  constructor({ container, itemHeight, totalItems, renderItem }) {
    this.container = container;
    this.itemHeight = itemHeight;
    this.totalItems = totalItems;
    this.renderItem = renderItem;
    this.container.addEventListener('scroll', this.handleScroll.bind(this));
  }
  
  handleScroll() {
    const scrollTop = this.container.scrollTop;
    const startIndex = Math.floor(scrollTop / this.itemHeight);
    const endIndex = Math.min(startIndex + 10, this.totalItems);
    this.renderItems(startIndex, endIndex);
  }
  
  renderItems(start, end) {
    this.container.innerHTML = '';
    for (let i = start; i < end; i++) {
      const item = this.renderItem(i);
      item.style.position = 'absolute';
      item.style.top = `${i * this.itemHeight}px`;
      this.container.appendChild(item);
    }
  }
}
```

#### B.10.2 后端性能优化

**数据库优化：**

| 技术 | 描述 |
|------|------|
| 索引优化 | 在查询条件列创建索引 |
| 查询优化 | 使用 JOIN 替代 N+1 查询 |
| 缓存 | 使用 Redis 缓存热点数据 |
| 读写分离 | 主库写，从库读 |
| 分库分表 | 处理大数据量 |

**API 优化：**

| 技术 | 描述 |
|------|------|
| 批量请求 | 合并多个请求 |
| 分页 | 限制返回数据量 |
| 缓存 | 使用 HTTP 缓存头 |
| 压缩 | 响应数据压缩 |

**代码示例：**

```javascript
// Redis 缓存示例
const redis = require('redis');
const client = redis.createClient();

async function getUser(id) {
  // 先从缓存获取
  const cached = await client.get(`user:${id}`);
  if (cached) {
    return JSON.parse(cached);
  }
  
  // 从数据库获取
  const user = await db.users.findOne({ id });
  
  // 存入缓存，设置过期时间
  await client.setEx(`user:${id}`, 3600, JSON.stringify(user));
  
  return user;
}

// 批量处理
async function getUsers(ids) {
  // 先获取缓存中的用户
  const cachedUsers = await Promise.all(
    ids.map(id => client.get(`user:${id}`))
  );
  
  // 找出需要从数据库获取的 ID
  const missingIds = ids.filter((_, index) => !cachedUsers[index]);
  
  // 从数据库获取
  const dbUsers = await db.users.find({ id: { $in: missingIds } });
  
  // 合并结果并更新缓存
  const result = {};
  ids.forEach((id, index) => {
    if (cachedUsers[index]) {
      result[id] = JSON.parse(cachedUsers[index]);
    } else {
      const user = dbUsers.find(u => u.id === id);
      result[id] = user;
      client.setEx(`user:${id}`, 3600, JSON.stringify(user));
    }
  });
  
  return result;
}
```

---

---

### B.11 操作系统进阶

#### B.11.1 内存管理深入

**内存分页机制：**

```
物理内存被划分为固定大小的页（通常 4KB 或 2MB）
虚拟地址空间同样被划分为页
页表记录虚拟页到物理页的映射
```

**页面置换算法：**

| 算法 | 描述 | 特点 |
|------|------|------|
| FIFO | 先进先出 | 简单但可能置换掉常用页面 |
| LRU | 最近最少使用 | 效果好，实现稍复杂 |
| LFU | 最不经常使用 | 考虑使用频率 |
| OPT | 最优置换 | 理论最优，不可实现 |

**内存泄漏检测：**

```bash
# Linux 内存泄漏检测
valgrind --leak-check=full ./program

# Node.js 内存分析
node --inspect --expose-gc app.js
# 在 Chrome 开发者工具中分析内存快照

# Python 内存分析
import tracemalloc
tracemalloc.start()

# 代码执行
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 memory usage ]")
for stat in top_stats[:10]:
    print(stat)
```

**内存优化策略：**

```typescript
// 对象池模式（减少 GC 压力）
class ObjectPool<T> {
  private pool: T[] = [];
  private factory: () => T;
  
  constructor(factory: () => T) {
    this.factory = factory;
  }
  
  acquire(): T {
    return this.pool.pop() || this.factory();
  }
  
  release(obj: T): void {
    this.pool.push(obj);
  }
}

// 使用对象池
const pool = new ObjectPool(() => ({ x: 0, y: 0 }));
const obj = pool.acquire();
// 使用对象
pool.release(obj);
```

#### B.11.2 文件系统深入

**文件系统层级：**

```
/ (根目录)
├── bin/        # 系统命令
├── etc/        # 配置文件
├── home/       # 用户目录
├── lib/        # 系统库
├── tmp/        # 临时文件（重启后清空）
├── usr/        # 用户程序
├── var/        # 可变数据（日志、缓存）
└── proc/       # 进程信息（虚拟文件系统）
```

**文件权限详解：**

```bash
# 权限表示
# r = 4 (读), w = 2 (写), x = 1 (执行)
# 用户 组 其他
# 755 = rwxr-xr-x

# 修改权限
chmod 755 script.sh  # rwxr-xr-x
chmod 644 file.txt   # rw-r--r--
chmod 700 secret/    # rwx------

# 修改所有者
chown user:group file.txt

# 特殊权限
chmod u+s program    # 设置 SUID（以所有者身份运行）
chmod g+s directory  # 设置 SGID（新建文件继承组）
chmod o+t directory  # 设置 sticky bit（只有所有者可删除）
```

**文件系统性能优化：**

```bash
# 查看磁盘 I/O
iostat -x 1 10

# 查看文件系统挂载信息
df -h

# 挂载优化选项
mount -o noatime,nodiratime /dev/sda1 /mnt/data

# 查看磁盘使用情况（按大小排序）
du -sh * | sort -rh

# 查找大文件
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

#### B.11.3 进程调度

**调度算法：**

| 算法 | 描述 | 适用场景 |
|------|------|---------|
| FCFS | 先来先服务 | 简单，适合批处理 |
| SJF | 短作业优先 | 平均等待时间最短 |
| RR | 时间片轮转 | 交互式系统 |
| Priority | 优先级调度 | 实时系统 |
| MLFQ | 多级反馈队列 | 通用系统 |

**进程状态转换：**

```
新进程 → 就绪队列 → 运行中 ↔ 阻塞（等待I/O） → 终止
                         ↓
                      就绪队列
```

**进程优先级：**

```bash
# 查看进程优先级
ps -eo pid,ppid,ni,cmd

# 调整进程优先级（nice 值：-20 到 19）
nice -n 5 ./program        # 启动时设置
renice -n 10 -p <PID>      # 运行时调整

# 实时优先级
chrt -f -p 99 <PID>        # 设置实时优先级
```

---

### B.12 网络进阶

#### B.12.1 TCP 协议深入

**TCP 状态机：**

```
LISTEN → SYN_SENT → SYN_RCVD → ESTABLISHED
                              ↓
                         FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED
                                   ↓
                              CLOSE_WAIT → LAST_ACK → CLOSED
```

**TCP 滑动窗口：**

```
发送方维护发送窗口（已发送未确认的数据）
接收方维护接收窗口（可用缓冲区大小）
通过滑动窗口实现流量控制
```

**TCP 拥塞控制：**

| 算法 | 描述 | 特点 |
|------|------|------|
| Reno | 慢启动 + 拥塞避免 | 经典算法 |
| Cubic | 基于窗口增长的立方函数 | Linux 默认 |
| BBR | 基于带宽和延迟的模型 | Google 提出 |

**TCP 连接问题排查：**

```bash
# 查看 TCP 连接状态
ss -tlnp

# 查看连接详情
netstat -antp

# 抓包分析
tcpdump -i eth0 port 80 -w capture.pcap

# 分析延迟
mtr --report google.com

# 测试带宽
iperf3 -c server_ip
```

#### B.12.2 HTTP/2 特性

**多路复用：**
- 单一 TCP 连接上并发多个请求/响应
- 消除队头阻塞

**头部压缩：**
- HPACK 算法压缩 HTTP 头部
- 维护头部字典，减少重复传输

**服务器推送：**
- 服务器主动推送资源
- 提前发送可能需要的资源

**HTTP/2 配置示例（Nginx）：**

```nginx
server {
    listen 443 ssl http2;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    # 启用 HTTP/2 推送
    http2_push_preload on;
    
    # 配置推送资源
    location = /index.html {
        http2_push /styles.css;
        http2_push /script.js;
    }
}
```

#### B.12.3 CDN 进阶配置

**缓存策略：**

```javascript
// 设置缓存头
app.use((req, res, next) => {
  // 静态资源缓存 1 年
  if (req.path.match(/\.(js|css|png|jpg|svg)$/)) {
    res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  }
  // HTML 不缓存或短时间缓存
  else {
    res.setHeader('Cache-Control', 'no-cache');
  }
  next();
});
```

**缓存失效策略：**

| 策略 | 描述 | 适用场景 |
|------|------|---------|
| 版本哈希 | 文件名包含哈希值 | 静态资源 |
| 时间戳 | URL 添加时间戳参数 | 动态内容 |
| CDN 刷新 | 主动清除 CDN 缓存 | 紧急更新 |

**CDN 回源配置：**

```javascript
// Cloudflare Worker 回源示例
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const cache = caches.default;
  const url = new URL(request.url);
  
  // 检查缓存
  let response = await cache.match(request);
  
  if (!response) {
    // 回源请求
    response = await fetch(request);
    
    // 缓存响应
    if (response.ok) {
      event.waitUntil(cache.put(request, response.clone()));
    }
  }
  
  return response;
}
```

---

### B.13 安全进阶

#### B.13.1 密码学基础

**哈希函数特性：**
- 确定性：相同输入产生相同输出
- 单向性：无法从哈希值还原原始数据
- 雪崩效应：微小输入变化导致完全不同的输出

**常见哈希算法：**

| 算法 | 输出长度 | 安全性 | 用途 |
|------|---------|--------|------|
| MD5 | 128 位 | 已破解 | 校验和 |
| SHA-1 | 160 位 | 不安全 | 历史系统 |
| SHA-256 | 256 位 | 安全 | 区块链、证书 |
| SHA-3 | 可变长度 | 安全 | 新兴标准 |

**对称加密 vs 非对称加密：**

| 特性 | 对称加密 | 非对称加密 |
|------|---------|-----------|
| 密钥 | 单密钥 | 公钥+私钥 |
| 速度 | 快 | 慢 |
| 用途 | 加密数据 | 密钥交换、签名 |
| 算法 | AES, DES | RSA, ECC |

**TLS 证书类型：**

| 类型 | 验证级别 | 适用场景 |
|------|---------|---------|
| DV | 域名验证 | 个人网站 |
| OV | 组织验证 | 企业网站 |
| EV | 扩展验证 | 金融机构 |

**证书链：**

```
用户浏览器
    ↓
服务器证书（由中间 CA 签发）
    ↓
中间 CA 证书（由根 CA 签发）
    ↓
根 CA 证书（自签名，内置在浏览器中）
```

#### B.13.2 身份认证进阶

**JWT 结构：**

```
Header.Payload.Signature

Header: {"alg": "HS256", "typ": "JWT"}
Payload: {"sub": "user123", "exp": 1717171200, "role": "admin"}
Signature: HMACSHA256(base64Url(header) + "." + base64Url(payload), secret)
```

**JWT 使用示例：**

```typescript
import jwt from 'jsonwebtoken';

// 生成 Token
const token = jwt.sign(
  { userId: '123', role: 'user' },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// 验证 Token
try {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  console.log('User ID:', decoded.userId);
} catch (err) {
  console.error('Invalid token:', err);
}

// 刷新 Token
function refreshToken(oldToken: string) {
  try {
    const decoded = jwt.verify(oldToken, process.env.JWT_SECRET, { ignoreExpiration: true });
    return jwt.sign(
      { userId: decoded.userId, role: decoded.role },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );
  } catch (err) {
    throw new Error('Invalid refresh token');
  }
}
```

**OAuth 2.0 流程：**

```
1. 用户授权：GET /authorize?client_id=xxx&redirect_uri=xxx&response_type=code&scope=openid
2. 获取授权码：回调返回 code
3. 获取令牌：POST /token 交换 code 获得 access_token 和 refresh_token
4. 访问资源：使用 access_token 访问 API
5. 刷新令牌：使用 refresh_token 获取新的 access_token
```

**OAuth 2.0 授权类型：**

| 类型 | 适用场景 |
|------|---------|
| Authorization Code | Web 应用 |
| Implicit | 纯前端应用 |
| Password | 信任的客户端 |
| Client Credentials | 服务间通信 |

**OpenID Connect：**
- 在 OAuth 2.0 基础上添加身份层
- 返回 ID Token（包含用户身份信息）
- 支持单点登录（SSO）

#### B.13.3 安全审计工具

```bash
# 代码安全扫描
npm install -g snyk
snyk test
snyk monitor

# 依赖漏洞检查
npm audit
pip check

# SQL 注入检测
sqlmap -u "http://example.com/login" --data "username=admin&password=test"

# XSS 检测
nmap --script http-xssed target.com

# SSL/TLS 检测
openssl s_client -connect example.com:443
ssllabs-scan example.com

# 密码强度检测
python3 -c "import zxcvbn; print(zxcvbn.zxcvbn('password123'))"
```

---

### B.14 性能监控进阶

#### B.14.1 指标监控

**RED 指标：**

| 指标 | 描述 | 计算公式 |
|------|------|---------|
| Rate | 请求速率 | 请求数 / 时间 |
| Error | 错误率 | 错误数 / 请求数 |
| Duration | 响应时间 | P50, P90, P95, P99 |

**USE 方法：**

| 资源 | 指标 |
|------|------|
| CPU | 使用率、饱和度、错误 |
| 内存 | 使用率、饱和度、错误 |
| 磁盘 | 使用率、饱和度、错误 |
| 网络 | 使用率、饱和度、错误 |

**自定义指标（Prometheus）：**

```typescript
import { Registry, Counter, Histogram } from 'prom-client';

const registry = new Registry();

// 计数器
const requestsCounter = new Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'endpoint', 'status']
});

// 直方图
const responseTimeHistogram = new Histogram({
  name: 'http_response_time_seconds',
  help: 'HTTP response time in seconds',
  labelNames: ['endpoint'],
  buckets: [0.1, 0.5, 1, 2, 5]
});

registry.registerMetric(requestsCounter);
registry.registerMetric(responseTimeHistogram);

// 使用中间件收集指标
app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    requestsCounter.inc({ 
      method: req.method, 
      endpoint: req.path, 
      status: res.statusCode 
    });
    responseTimeHistogram.observe({ endpoint: req.path }, duration);
  });
  
  next();
});

// 暴露指标端点
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', registry.contentType);
  res.send(await registry.metrics());
});
```

#### B.14.2 日志管理

**日志级别详解：**

| 级别 | 使用场景 | 示例 |
|------|---------|------|
| DEBUG | 详细调试信息 | 函数调用参数、变量值 |
| INFO | 正常业务流程 | 用户登录、订单创建 |
| WARN | 潜在问题 | 缓存未命中、重试操作 |
| ERROR | 可恢复错误 | 数据库连接失败、API 调用失败 |
| FATAL | 致命错误 | 服务无法启动、数据丢失 |

**结构化日志格式：**

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "service": "user-service",
  "trace_id": "abc123",
  "span_id": "def456",
  "message": "User logged in",
  "context": {
    "user_id": "12345",
    "ip_address": "192.168.1.1",
    "user_agent": "Mozilla/5.0..."
  }
}
```

**日志聚合示例（ELK Stack）：**

```yaml
# filebeat.yml 配置
filebeat.inputs:
  - type: log
    paths:
      - /var/log/myapp/*.log

output.elasticsearch:
  hosts: ["elasticsearch:9200"]

setup.kibana:
  host: "kibana:5601"

# Logstash 过滤器
filter {
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:message}" }
  }
  date {
    match => [ "timestamp", "ISO8601" ]
  }
}
```

#### B.14.3 分布式追踪

**追踪上下文传播：**

```typescript
import { trace, context } from '@opentelemetry/api';

// 创建追踪器
const tracer = trace.getTracer('my-service');

// 创建 span
async function handleRequest(req) {
  return tracer.startActiveSpan('handle-request', async (span) => {
    try {
      span.setAttribute('request.method', req.method);
      span.setAttribute('request.path', req.path);
      
      const result = await processRequest(req);
      span.setStatus({ code: SpanStatusCode.OK });
      return result;
    } catch (error) {
      span.setStatus({ 
        code: SpanStatusCode.ERROR, 
        message: error.message 
      });
      throw error;
    } finally {
      span.end();
    }
  });
}

// 跨服务传播
async function callServiceB(data) {
  const span = trace.getSpan(context.active());
  const headers = {};
  
  // 注入追踪上下文到请求头
  trace.getTracerProvider().getTracer('my-service')
    .getActiveSpanProcessor()
    .inject(context.active(), headers);
  
  return fetch('http://service-b/api', {
    method: 'POST',
    headers: { ...headers, 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
}
```

**追踪工具对比：**

| 工具 | 特点 | 适用场景 |
|------|------|---------|
| Jaeger | 开源、轻量 | 中小型系统 |
| Zipkin | 简单易用 | 微服务架构 |
| OpenTelemetry | 标准化 API | 多云环境 |
| Datadog APM | 全链路追踪 | 企业级 |

---

### B.15 容器进阶

#### B.15.1 Docker 网络

**网络模式详解：**

| 模式 | 描述 | 隔离性 |
|------|------|--------|
| bridge | 默认模式，虚拟网桥 | 容器间可通信 |
| host | 共享宿主机网络 | 无隔离 |
| none | 无网络连接 | 完全隔离 |
| container | 共享另一个容器网络 | 与目标容器共享 |
| overlay | 跨主机网络 | Swarm 集群 |

**自定义网络：**

```bash
# 创建自定义网络
docker network create --driver bridge my-network

# 连接容器到网络
docker run --network my-network --name app1 myapp
docker run --network my-network --name app2 myapp

# 容器间通信
docker exec app1 ping app2  # 使用容器名解析

# 查看网络详情
docker network inspect my-network
```

**Docker Compose 网络：**

```yaml
version: '3.8'
services:
  web:
    build: .
    networks:
      - frontend
      - backend
  
  api:
    build: ./api
    networks:
      - backend
  
  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # 不对外暴露
```

#### B.15.2 Docker 存储

**存储驱动对比：**

| 驱动 | 特点 | 适用场景 |
|------|------|---------|
| overlay2 | 高效、分层 | 推荐默认 |
| aufs | 成熟、兼容性好 | 旧系统 |
| btrfs | 快照支持 | 特定场景 |
| zfs | 高级特性 | 企业存储 |

**卷挂载类型：**

```yaml
version: '3.8'
services:
  app:
    image: myapp
    volumes:
      # 命名卷（推荐）
      - data:/app/data
      
      # 绑定挂载（开发用）
      - ./src:/app/src
      
      # tmpfs（临时存储）
      - type: tmpfs
        target: /tmp
      
      # 只读挂载
      - ./config:/app/config:ro

volumes:
  data:
    driver: local
```

**卷备份与恢复：**

```bash
# 备份卷
docker run --rm -v my-volume:/data -v $(pwd):/backup busybox \
  tar cvf /backup/backup.tar /data

# 恢复卷
docker run --rm -v my-volume:/data -v $(pwd):/backup busybox \
  tar xvf /backup/backup.tar -C /data
```

#### B.15.3 Kubernetes 进阶

**Pod 生命周期：**

```
Pending → Running → Succeeded/Failed/Unknown

重启策略：Always / OnFailure / Never
```

**探针配置：**

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: app
      image: myapp
      ports:
        - containerPort: 3000
      
      # 存活探针
      livenessProbe:
        httpGet:
          path: /health
          port: 3000
        initialDelaySeconds: 10
        periodSeconds: 5
        failureThreshold: 3
      
      # 就绪探针
      readinessProbe:
        tcpSocket:
          port: 3000
        initialDelaySeconds: 5
        periodSeconds: 3
      
      # 启动探针
      startupProbe:
        exec:
          command: ["node", "-e", "require('./server').start()"]
        failureThreshold: 30
        periodSeconds: 10
```

**资源限制：**

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: app
      image: myapp
      resources:
        requests:
          memory: "128Mi"
          cpu: "100m"
        limits:
          memory: "256Mi"
          cpu: "200m"
```

**ConfigMap 与 Secret：**

```yaml
# ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  NODE_ENV: production
  API_URL: https://api.example.com

# Secret（base64 编码）
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  DATABASE_PASSWORD: cGFzc3dvcmQ=
  API_KEY: dGVzdC1rZXk=
```

---

### B.16 故障排查方法论

#### B.16.1 系统化排查流程

```
1. 定义问题：明确现象、范围、频率
2. 收集信息：日志、指标、配置
3. 形成假设：基于信息提出可能原因
4. 验证假设：设计测试验证
5. 实施修复：应用解决方案
6. 验证修复：确认问题解决
7. 记录总结：文档化问题和解决方案
```

#### B.16.2 常见问题排查

**高 CPU 使用率：**

```bash
# 查找高 CPU 进程
top -o %CPU
htop

# 分析进程线程
ps -T -p <PID>

# 分析 Java 线程
jstack <PID> | grep -A 10 "RUNNABLE"

# 分析 Node.js
node --inspect --inspect-brk app.js
```

**内存泄漏：**

```bash
# 监控内存使用
free -h
vmstat 1 10

# 分析内存快照（Node.js）
node --expose-gc app.js
# 在 Chrome DevTools 中分析

# Python 内存分析
pip install memory_profiler
@profile
def my_function():
    # 代码
    pass
```

**网络问题：**

```bash
# 检查网络连通性
ping google.com
traceroute google.com
mtr google.com

# 检查端口
nc -zv localhost 3000
ss -tlnp | grep 3000

# 抓包分析
tcpdump -i eth0 port 80 -w capture.pcap
wireshark capture.pcap

# DNS 问题
dig example.com
nslookup example.com
```

**数据库慢查询：**

```sql
-- PostgreSQL 慢查询日志
SET log_min_duration_statement = 100; -- 记录超过 100ms 的查询

-- 查看正在运行的查询
SELECT pid, query, now() - query_start as duration
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY duration DESC;

-- 分析查询计划
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123;

-- MySQL 慢查询日志
slow_query_log = ON
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2
```

#### B.16.3 应急响应流程

**事故响应步骤：**

```
1. 检测：监控告警、用户反馈
2. 确认：验证问题确实存在
3. 评估：影响范围、严重程度
4. 通知：相关人员、用户
5. 缓解：临时解决方案
6. 修复：根本原因修复
7. 验证：确认服务恢复
8. 复盘：总结经验教训
```

**严重程度分级：**

| 级别 | 描述 | 响应时间 |
|------|------|---------|
| P0 | 系统完全不可用 | 立即 |
| P1 | 核心功能故障 | 15 分钟内 |
| P2 | 次要功能故障 | 1 小时内 |
| P3 | 轻微问题 | 24 小时内 |

---

### B.17 测试策略

#### B.17.1 测试金字塔

```
         ╱╲
        ╱  ╲         E2E 测试（少）
       ╱    ╲
      ╱──────╲
     ╱        ╲      集成测试（中）
    ╱          ╲
   ╱────────────╲
  ╱              ╲   单元测试（多）
 ╱────────────────╲
```

**各层测试的特点：**

| 层级 | 速度 | 成本 | 维护难度 | 覆盖范围 |
|------|------|------|---------|---------|
| 单元测试 | 快（毫秒级） | 低 | 低 | 单个函数/类 |
| 集成测试 | 中（秒级） | 中 | 中 | 模块间交互 |
| E2E 测试 | 慢（分钟级） | 高 | 高 | 完整用户流程 |

**黄金比例（实践经验）：**
- 单元测试占 70%——快速验证核心逻辑
- 集成测试占 20%——验证模块间协作
- E2E 测试占 10%——验证关键用户路径

#### B.17.2 单元测试

```javascript
// Jest 测试框架示例
// math.js
export function add(a, b) {
  return a + b;
}

export function divide(a, b) {
  if (b === 0) {
    throw new Error('Division by zero');
  }
  return a / b;
}

// math.test.js
import { add, divide } from './math';

describe('Math functions', () => {
  describe('add', () => {
    it('should add two positive numbers', () => {
      expect(add(2, 3)).toBe(5);
    });
    
    it('should handle negative numbers', () => {
      expect(add(-1, 1)).toBe(0);
      expect(add(-1, -1)).toBe(-2);
    });
    
    it('should handle decimal numbers', () => {
      expect(add(0.1, 0.2)).toBeCloseTo(0.3);
    });
  });
  
  describe('divide', () => {
    it('should divide two numbers', () => {
      expect(divide(10, 2)).toBe(5);
    });
    
    it('should throw when dividing by zero', () => {
      expect(() => divide(10, 0)).toThrow('Division by zero');
    });
  });
});
```

```python
# pytest 测试框架示例
# test_math.py
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (0.1, 0.2, 0.3),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Fixture 示例
@pytest.fixture
def test_db():
    # 设置测试数据库
    db = create_test_database()
    yield db
    # 清理
    drop_test_database(db)

def test_user_creation(test_db):
    user = test_db.create_user("Alice", "alice@example.com")
    assert user.name == "Alice"
```

#### B.17.3 集成测试

```javascript
// API 集成测试（Supertest）
import request from 'supertest';
import app from '../app';

describe('User API', () => {
  describe('POST /api/users', () => {
    it('should create a new user', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({
          name: 'Alice',
          email: 'alice@example.com',
          age: 30,
        })
        .expect(201);
      
      expect(response.body.data).toHaveProperty('id');
      expect(response.body.data.name).toBe('Alice');
    });
    
    it('should return 400 for invalid input', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ name: '' })
        .expect(400);
      
      expect(response.body.error).toBeDefined();
    });
  });
  
  describe('GET /api/users/:id', () => {
    it('should return a user by id', async () => {
      const user = await createTestUser();
      
      const response = await request(app)
        .get(`/api/users/${user.id}`)
        .expect(200);
      
      expect(response.body.data.name).toBe(user.name);
    });
    
    it('should return 404 for non-existent user', async () => {
      await request(app)
        .get('/api/users/99999')
        .expect(404);
    });
  });
});
```

```python
# FastAPI 集成测试
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/users", json={
        "name": "Alice",
        "email": "alice@example.com",
    })
    assert response.status_code == 201
    data = response.json()["data"]
    assert data["name"] == "Alice"
    assert "id" in data

def test_get_user():
    # 先创建用户
    create_response = client.post("/api/users", json={
        "name": "Bob",
        "email": "bob@example.com",
    })
    user_id = create_response.json()["data"]["id"]
    
    # 查询用户
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Bob"
```

#### B.17.4 E2E 测试

```javascript
// Cypress E2E 测试
describe('User Login Flow', () => {
  beforeEach(() => {
    cy.visit('/login');
  });
  
  it('should login successfully with valid credentials', () => {
    cy.get('[data-testid="email-input"]').type('alice@example.com');
    cy.get('[data-testid="password-input"]').type('correct-password');
    cy.get('[data-testid="login-button"]').click();
    
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="welcome-message"]').should('contain', 'Welcome, Alice');
  });
  
  it('should show error with invalid credentials', () => {
    cy.get('[data-testid="email-input"]').type('alice@example.com');
    cy.get('[data-testid="password-input"]').type('wrong-password');
    cy.get('[data-testid="login-button"]').click();
    
    cy.get('[data-testid="error-message"]')
      .should('be.visible')
      .and('contain', 'Invalid credentials');
  });
  
  it('should validate email format', () => {
    cy.get('[data-testid="email-input"]').type('invalid-email');
    cy.get('[data-testid="password-input"]').type('password123');
    cy.get('[data-testid="login-button"]').click();
    
    cy.get('[data-testid="email-error"]')
      .should('be.visible')
      .and('contain', 'Please enter a valid email');
  });
});
```

#### B.17.5 Mock 与 Stub

```javascript
// Mock 外部依赖
jest.mock('../services/email');
import { sendEmail } from '../services/email';
import { signup } from './auth';

describe('User Signup', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });
  
  it('should send welcome email after signup', async () => {
    sendEmail.mockResolvedValue({ success: true });
    
    const user = await signup({
      name: 'Alice',
      email: 'alice@example.com',
    });
    
    expect(sendEmail).toHaveBeenCalledWith({
      to: 'alice@example.com',
      template: 'welcome',
      data: { name: 'Alice' },
    });
  });
  
  it('should still create user when email fails', async () => {
    sendEmail.mockRejectedValue(new Error('Email service down'));
    
    const user = await signup({
      name: 'Bob',
      email: 'bob@example.com',
    });
    
    expect(user).toBeDefined();
    expect(user.name).toBe('Bob');
  });
});
```

#### B.17.6 测试最佳实践

| 原则 | 说明 | 示例 |
|------|------|------|
| **FIRST 原则** | Fast, Independent, Repeatable, Self-validating, Timely |
| **单一断言** | 每个测试只验证一个行为 | 一个 it/assert 只测一个功能点 |
| **避免测试实现细节** | 测试行为而非实现 | 测试输出而非内部调用顺序 |
| **使用测试工厂** | 复用测试数据构建 | 使用 factory_boy/faker 生成数据 |
| **测试边界条件** | 空值、边界值、异常值 | 空数组、最大最小值、null |
| **维护测试可读性** | 测试即文档 | 描述清晰的测试名称和结构 |

**测试命名规范：**

```javascript
// 命名模式：[unit/function] should [expected behavior] when [condition]
describe('ShoppingCart', () => {
  it('should calculate total correctly when adding multiple items', () => {
    // ...
  });
  
  it('should apply discount when coupon code is valid', () => {
    // ...
  });
  
  it('should throw error when adding out-of-stock item', () => {
    // ...
  });
});
```

#### B.17.7 测试覆盖率

| 覆盖率类型 | 定义 | 目标值 |
|-----------|------|--------|
| 行覆盖率 | 代码行被执行的比例 | 80%+ |
| 分支覆盖率 | 条件分支被覆盖的比例 | 70%+ |
| 函数覆盖率 | 函数被调用的比例 | 90%+ |
| 语句覆盖率 | 语句被执行的比例 | 80%+ |

```javascript
// 运行覆盖率报告
// npm test -- --coverage
// npx jest --coverage

// 覆盖率配置（jest.config.js）
module.exports = {
  collectCoverage: true,
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
    './src/components/': {
      lines: 90,
    },
  },
  coveragePathIgnorePatterns: [
    '/node_modules/',
    '/__tests__/',
    '/types/',
  ],
};
```

---

### B.18 API 设计模式

#### B.18.1 RESTful API 设计原则

| 原则 | 说明 | 示例 |
|------|------|------|
| 资源导向 | 用名词命名资源，而非动词 | `/users` 而非 `/getUsers` |
| HTTP 方法语义 | GET 查、POST 增、PUT 改、DELETE 删 | `GET /users/:id` |
| 状态码规范 | 使用标准 HTTP 状态码 | 200 成功、201 创建、404 未找到 |
| 版本管理 | 通过 URL 或请求头管理版本 | `/api/v1/users` |
| 分页标准 | 统一的分页响应格式 | `{ data: [...], page: 1, total: 50 }` |
| 错误格式 | 统一的错误响应格式 | `{ error: { code, message } }` |

**API 端点命名规范：**

```
# 资源列表
GET    /api/users                    # 获取用户列表
POST   /api/users                    # 创建用户

# 单个资源
GET    /api/users/:id                # 获取单个用户
PUT    /api/users/:id                # 更新用户（全量）
PATCH  /api/users/:id                # 更新用户（部分）
DELETE /api/users/:id                # 删除用户

# 资源关系
GET    /api/users/:id/posts          # 获取用户的帖子
POST   /api/users/:id/posts          # 创建用户的帖子
GET    /api/posts/:id/comments       # 获取帖子的评论

# 操作（动词在最后）
POST   /api/users/:id/activate       # 激活用户
POST   /api/orders/:id/cancel        # 取消订单
POST   /api/payments/:id/refund      # 退款
```

#### B.18.2 API 错误处理规范

```typescript
// 统一错误格式
interface ApiError {
  code: string;
  message: string;
  details?: Record<string, string[]>;
  requestId?: string;
  timestamp?: string;
}

// 错误码规范
const ErrorCodes = {
  // 4xx 客户端错误
  VALIDATION_ERROR: 'VALIDATION_ERROR',
  UNAUTHORIZED: 'UNAUTHORIZED',
  FORBIDDEN: 'FORBIDDEN',
  NOT_FOUND: 'NOT_FOUND',
  RATE_LIMIT_EXCEEDED: 'RATE_LIMIT_EXCEEDED',
  CONFLICT: 'CONFLICT',
  
  // 5xx 服务器错误
  INTERNAL_ERROR: 'INTERNAL_ERROR',
  SERVICE_UNAVAILABLE: 'SERVICE_UNAVAILABLE',
  DATABASE_ERROR: 'DATABASE_ERROR',
  EXTERNAL_SERVICE_ERROR: 'EXTERNAL_SERVICE_ERROR',
} as const;

// 错误处理示例
app.post('/api/orders', async (req, res) => {
  try {
    const order = await createOrder(req.body);
    res.status(201).json({ data: order });
  } catch (error) {
    if (error instanceof ValidationError) {
      return res.status(400).json({
        code: 'VALIDATION_ERROR',
        message: 'Invalid order data',
        details: error.errors,
      });
    }
    
    if (error instanceof ConflictError) {
      return res.status(409).json({
        code: 'CONFLICT',
        message: 'Order already exists',
      });
    }
    
    // 未知错误
    console.error('Unexpected error creating order:', error);
    res.status(500).json({
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred',
      requestId: req.id,
    });
  }
});
```

#### B.18.3 分页与过滤

```typescript
// 分页查询参数
interface PaginationParams {
  page?: number;        // 页码，从1开始
  limit?: number;       // 每页数量，默认20
  sort?: string;        // 排序字段
  order?: 'asc' | 'desc';  // 排序方向
  search?: string;      // 搜索关键词
  filters?: Record<string, any>;  // 过滤条件
}

// 分页响应
interface PaginatedResponse<T> {
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNext: boolean;
    hasPrev: boolean;
  };
}

// 游标分页（适合实时数据）
interface CursorPagination {
  data: T[];
  cursor: {
    next: string | null;
    prev: string | null;
    hasMore: boolean;
  };
}

// 实现示例
async function listUsers(req, res) {
  const { page = 1, limit = 20, sort = 'created_at', order = 'desc', search } = req.query;
  
  const where = search
    ? { OR: [{ name: { contains: search } }, { email: { contains: search } }] }
    : {};
  
  const [users, total] = await Promise.all([
    db.users.findMany({
      where,
      skip: (Number(page) - 1) * Number(limit),
      take: Number(limit),
      orderBy: { [sort]: order },
    }),
    db.users.count({ where }),
  ]);
  
  res.json({
    data: users,
    pagination: {
      page: Number(page),
      limit: Number(limit),
      total,
      totalPages: Math.ceil(total / Number(limit)),
      hasNext: Number(page) * Number(limit) < total,
      hasPrev: Number(page) > 1,
    },
  });
}
```

#### B.18.4 API 安全

```typescript
// 速率限制（Rate Limiting）
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,    // 15分钟窗口
  max: 100,                      // 每个 IP 最多100个请求
  standardHeaders: true,
  message: {
    code: 'RATE_LIMIT_EXCEEDED',
    message: 'Too many requests, please try again later.',
  },
});

app.use('/api/', limiter);

// API 认证中间件链
app.use('/api/admin', authenticate);           // 先认证
app.use('/api/admin', authorize('admin'));     // 再授权
app.use('/api/admin', auditLog);               // 审计日志

// 请求大小限制
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// CORS 白名单
const allowedOrigins = [
  'https://example.com',
  'https://admin.example.com',
];

app.use(cors({
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
}));
```

#### B.18.5 API 文档

```javascript
// Swagger/OpenAPI 配置示例
const swaggerOptions = {
  openapi: '3.0.0',
  info: {
    title: 'User Management API',
    version: '1.0.0',
    description: 'API for managing users and their posts',
  },
  servers: [
    { url: 'https://api.example.com/v1', description: 'Production' },
    { url: 'https://staging-api.example.com/v1', description: 'Staging' },
  ],
  components: {
    securitySchemes: {
      bearerAuth: {
        type: 'http',
        scheme: 'bearer',
        bearerFormat: 'JWT',
      },
    },
  },
  paths: {
    '/users': {
      get: {
        summary: 'Get users list',
        security: [{ bearerAuth: [] }],
        parameters: [
          { name: 'page', in: 'query', schema: { type: 'integer' } },
          { name: 'limit', in: 'query', schema: { type: 'integer' } },
          { name: 'search', in: 'query', schema: { type: 'string' } },
        ],
        responses: {
          '200': {
            description: 'Successful response',
            content: {
              'application/json': {
                schema: {
                  type: 'object',
                  properties: {
                    data: { type: 'array', items: { $ref: '#/components/schemas/User' } },
                    pagination: { $ref: '#/components/schemas/Pagination' },
                  },
                },
              },
            },
          },
        },
      },
    },
  },
};
```

---

### B.19 设计模式

#### B.19.1 创建型模式

```typescript
// 单例模式（Singleton）
class DatabaseConnection {
  private static instance: DatabaseConnection;
  private connection: any;
  
  private constructor() {
    this.connection = this.createConnection();
  }
  
  static getInstance(): DatabaseConnection {
    if (!DatabaseConnection.instance) {
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }
  
  async query(sql: string): Promise<any> {
    return this.connection.query(sql);
  }
  
  private createConnection() {
    console.log('Creating database connection...');
    return { query: async (sql: string) => console.log(`Executing: ${sql}`) };
  }
}

// 使用
const db1 = DatabaseConnection.getInstance();
const db2 = DatabaseConnection.getInstance();
console.log(db1 === db2); // true

// 工厂模式（Factory）
interface Logger {
  log(message: string): void;
}

class ConsoleLogger implements Logger {
  log(message: string): void {
    console.log(`[Console] ${message}`);
  }
}

class FileLogger implements Logger {
  constructor(private filePath: string) {}
  log(message: string): void {
    console.log(`[File] Writing to ${this.filePath}: ${message}`);
  }
}

class CloudLogger implements Logger {
  log(message: string): void {
    console.log(`[Cloud] Sending to cloud: ${message}`);
  }
}

class LoggerFactory {
  static createLogger(type: string, options?: any): Logger {
    switch (type) {
      case 'console':
        return new ConsoleLogger();
      case 'file':
        return new FileLogger(options?.filePath || './logs/app.log');
      case 'cloud':
        return new CloudLogger();
      default:
        throw new Error(`Unknown logger type: ${type}`);
    }
  }
}

// 使用
const logger = LoggerFactory.createLogger('console');
logger.log('Application started');

// 建造者模式（Builder）
class QueryBuilder {
  private table: string = '';
  private conditions: string[] = [];
  private orderByField: string = '';
  private orderDirection: string = 'ASC';
  private limitValue: number = 0;
  private offset: number = 0;
  
  from(table: string): this {
    this.table = table;
    return this;
  }
  
  where(field: string, operator: string, value: any): this {
    this.conditions.push(`${field} ${operator} ${typeof value === 'string' ? `'${value}'` : value}`);
    return this;
  }
  
  orderBy(field: string, direction: 'ASC' | 'DESC' = 'ASC'): this {
    this.orderByField = field;
    this.orderDirection = direction;
    return this;
  }
  
  limit(n: number): this {
    this.limitValue = n;
    return this;
  }
  
  build(): string {
    let query = `SELECT * FROM ${this.table}`;
    
    if (this.conditions.length > 0) {
      query += ` WHERE ${this.conditions.join(' AND ')}`;
    }
    
    if (this.orderByField) {
      query += ` ORDER BY ${this.orderByField} ${this.orderDirection}`;
    }
    
    if (this.limitValue > 0) {
      query += ` LIMIT ${this.limitValue}`;
    }
    
    if (this.offset > 0) {
      query += ` OFFSET ${this.offset}`;
    }
    
    return query;
  }
}

// 使用
const query = new QueryBuilder()
  .from('users')
  .where('age', '>', 18)
  .where('status', '=', 'active')
  .orderBy('name', 'ASC')
  .limit(10)
  .build();

console.log(query);
// SELECT * FROM users WHERE age > 18 AND status = 'active' ORDER BY name ASC LIMIT 10
```

#### B.19.2 结构型模式

```typescript
// 适配器模式（Adapter）
// 场景：第三方支付库与我们的系统接口不同

// 我们系统的统一支付接口
interface PaymentProcessor {
  processPayment(amount: number, currency: string): Promise<PaymentResult>;
  refundPayment(transactionId: string): Promise<RefundResult>;
}

interface PaymentResult {
  success: boolean;
  transactionId: string;
  message: string;
}

interface RefundResult {
  success: boolean;
  refundId: string;
}

// 第三方 Stripe 支付（不同接口）
class StripeSDK {
  async charge(amountInCents: number, currencyCode: string): Promise<any> {
    // Stripe 原生接口
    return { id: 'stripe_123', status: 'succeeded' };
  }
  
  async refund(chargeId: string): Promise<any> {
    return { id: 'refund_456', status: 'succeeded' };
  }
}

// 适配器
class StripeAdapter implements PaymentProcessor {
  private stripe: StripeSDK;
  
  constructor(stripe: StripeSDK) {
    this.stripe = stripe;
  }
  
  async processPayment(amount: number, currency: string): Promise<PaymentResult> {
    const result = await this.stripe.charge(amount * 100, currency);
    return {
      success: result.status === 'succeeded',
      transactionId: result.id,
      message: 'Payment successful',
    };
  }
  
  async refundPayment(transactionId: string): Promise<RefundResult> {
    const result = await this.stripe.refund(transactionId);
    return {
      success: result.status === 'succeeded',
      refundId: result.id,
    };
  }
}

// 装饰器模式（Decorator）
interface Coffee {
  cost(): number;
  description(): string;
}

class SimpleCoffee implements Coffee {
  cost(): number { return 10; }
  description(): string { return 'Simple coffee'; }
}

class MilkDecorator implements Coffee {
  constructor(private coffee: Coffee) {}
  
  cost(): number { return this.coffee.cost() + 3; }
  description(): string { return this.coffee.description() + ', milk'; }
}

class SugarDecorator implements Coffee {
  constructor(private coffee: Coffee) {}
  
  cost(): number { return this.coffee.cost() + 1; }
  description(): string { return this.coffee.description() + ', sugar'; }
}

class WhippedCreamDecorator implements Coffee {
  constructor(private coffee: Coffee) {}
  
  cost(): number { return this.coffee.cost() + 5; }
  description(): string { return this.coffee.description() + ', whipped cream'; }
}

// 使用
let coffee: Coffee = new SimpleCoffee();
coffee = new MilkDecorator(coffee);
coffee = new SugarDecorator(coffee);
coffee = new WhippedCreamDecorator(coffee);

console.log(coffee.description());  // "Simple coffee, milk, sugar, whipped cream"
console.log(coffee.cost());          // 19
```

#### B.19.3 行为型模式

```typescript
// 观察者模式（Observer）
interface Observer {
  update(event: string, data: any): void;
}

class EventBus {
  private observers: Map<string, Set<Observer>> = new Map();
  
  subscribe(event: string, observer: Observer): void {
    if (!this.observers.has(event)) {
      this.observers.set(event, new Set());
    }
    this.observers.get(event)!.add(observer);
  }
  
  unsubscribe(event: string, observer: Observer): void {
    this.observers.get(event)?.delete(observer);
  }
  
  publish(event: string, data: any): void {
    this.observers.get(event)?.forEach(observer => {
      observer.update(event, data);
    });
  }
}

// 具体观察者
class EmailService implements Observer {
  update(event: string, data: any): void {
    if (event === 'user.created') {
      console.log(`Sending welcome email to ${data.email}`);
    }
  }
}

class AuditService implements Observer {
  update(event: string, data: any): void {
    console.log(`Audit log: ${event} - ${JSON.stringify(data)}`);
  }
}

class NotificationService implements Observer {
  update(event: string, data: any): void {
    if (event === 'order.shipped') {
      console.log(`Sending notification: Order ${data.orderId} shipped`);
    }
  }
}

// 使用
const eventBus = new EventBus();
const emailService = new EmailService();
const auditService = new AuditService();

eventBus.subscribe('user.created', emailService);
eventBus.subscribe('user.created', auditService);
eventBus.subscribe('order.shipped', new NotificationService());

eventBus.publish('user.created', { id: 1, email: 'alice@example.com' });
eventBus.publish('order.shipped', { orderId: 'ORD-123' });

// 策略模式（Strategy）
interface SortStrategy {
  sort<T>(items: T[]): T[];
}

class QuickSortStrategy implements SortStrategy {
  sort<T>(items: T[]): T[] {
    if (items.length <= 1) return items;
    const pivot = items[Math.floor(items.length / 2)];
    const left = items.filter(x => x < pivot);
    const right = items.filter(x => x > pivot);
    const equal = items.filter(x => x === pivot);
    return [...this.sort(left), ...equal, ...this.sort(right)];
  }
}

class MergeSortStrategy implements SortStrategy {
  sort<T>(items: T[]): T[] {
    if (items.length <= 1) return items;
    const mid = Math.floor(items.length / 2);
    const left = this.sort(items.slice(0, mid));
    const right = this.sort(items.slice(mid));
    return this.merge(left, right);
  }
  
  private merge<T>(left: T[], right: T[]): T[] {
    const result: T[] = [];
    let i = 0, j = 0;
    
    while (i < left.length && j < right.length) {
      if (left[i] < right[j]) {
        result.push(left[i++]);
      } else {
        result.push(right[j++]);
      }
    }
    
    return [...result, ...left.slice(i), ...right.slice(j)];
  }
}

class Sorter {
  private strategy: SortStrategy;
  
  constructor(strategy: SortStrategy) {
    this.strategy = strategy;
  }
  
  setStrategy(strategy: SortStrategy) {
    this.strategy = strategy;
  }
  
  sort<T>(items: T[]): T[] {
    return this.strategy.sort(items);
  }
}

// 使用
const sorter = new Sorter(new QuickSortStrategy());
const numbers = [5, 2, 8, 1, 9, 3];
console.log(sorter.sort(numbers)); // [1, 2, 3, 5, 8, 9]

// 切换策略
sorter.setStrategy(new MergeSortStrategy());
console.log(sorter.sort(numbers));
```

#### B.19.4 设计模式选择指南

| 模式 | 类型 | 解决的问题 | 适用场景 |
|------|------|-----------|---------|
| 单例 | 创建型 | 确保全局只有一个实例 | 数据库连接、配置管理 |
| 工厂 | 创建型 | 封装对象创建逻辑 | 复杂对象创建、切换实现 |
| 建造者 | 创建型 | 分步构建复杂对象 | SQL 构建器、配置对象 |
| 适配器 | 结构型 | 接口不兼容 | 第三方库集成 |
| 装饰器 | 结构型 | 动态添加功能 | 中间件、日志、缓存 |
| 代理 | 结构型 | 控制对象访问 | 懒加载、权限控制 |
| 观察者 | 行为型 | 一对多通知 | 事件系统、消息队列 |
| 策略 | 行为型 | 算法可切换 | 排序、支付、验证 |
| 命令 | 行为型 | 请求封装 | 撤销、事务、队列 |
| 模板方法 | 行为型 | 算法框架固定 | 数据处理流程 |

---

### B.20 云服务基础

#### B.20.1 云服务模型

| 模型 | 描述 | 用户管理 | 提供商管理 | 示例 |
|------|------|---------|-----------|------|
| IaaS | 基础设施即服务 | 应用、数据、运行时、部分安全 | 虚拟化、服务器、存储、网络 | AWS EC2, GCP Compute |
| PaaS | 平台即服务 | 应用、数据 | 运行时、中间件、OS、基础设施 | Vercel, Railway |
| SaaS | 软件即服务 | 数据、配置 | 全部底层 | Gmail, Notion |
| FaaS | 函数即服务 | 函数代码 | 全部底层 | AWS Lambda, Cloudflare Workers |

#### B.20.2 主流云服务商

| 服务商 | 优势 | 适合场景 | 主要产品 |
|--------|------|---------|---------|
| AWS | 生态最全、功能最多 | 企业级、复杂架构 | EC2、S3、Lambda、RDS |
| Google Cloud | 数据/AI 能力强 | 数据分析、机器学习 | Cloud Run、BigQuery |
| Azure | .NET 集成好 | 微软生态客户 | Azure Functions、SQL |
| Vercel | 前端部署最佳 | Next.js、前端项目 | Edge Functions、Serverless |
| Cloudflare | 全球 CDN、安全 | 边缘计算、静态站点 | Workers、Pages、R2 |
| Railway | 部署最简单 | 全栈小项目 | 一键部署、数据库 |
| Fly.io | 全球部署 | 需要全球覆盖的应用 | Fly Machines、Postgres |
| DigitalOcean | 价格透明 | 中小型项目 | Droplets、App Platform |

#### B.20.3 服务器部署流程

```bash
# 1. 服务器初始设置
ssh root@your-server-ip

# 系统更新
apt update && apt upgrade -y

# 创建普通用户
adduser deploy
usermod -aG sudo deploy

# 配置 SSH 密钥
mkdir -p /home/deploy/.ssh
echo "your-public-key" >> /home/deploy/.ssh/authorized_keys
chown -R deploy:deploy /home/deploy/.ssh
chmod 700 /home/deploy/.ssh
chmod 600 /home/deploy/.ssh/authorized_keys

# 2. 安装基础软件
apt install -y nginx postgresql redis-server certbot python3-certbot-nginx

# 3. 安装 Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# 4. 安装 Docker
curl -fsSL https://get.docker.com | sh
usermod -aG docker deploy

# 5. 配置 Nginx 反向代理
cat > /etc/nginx/sites-available/myapp << 'EOF'
server {
    listen 80;
    server_name example.com;
    
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /var/www/myapp/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
EOF

ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx

# 6. 配置 HTTPS
certbot --nginx -d example.com

# 7. 配置防火墙
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

#### B.20.4 数据库托管服务

| 服务 | 类型 | 免费额度 | 适合场景 |
|------|------|---------|---------|
| Supabase | PostgreSQL | 500MB | 全栈项目，含实时功能 |
| PlanetScale | MySQL | 1GB | 无服务器 MySQL |
| Neon | PostgreSQL | 500MB | Serverless PostgreSQL |
| MongoDB Atlas | MongoDB | 512MB | 文档数据库 |
| Redis Cloud | Redis | 30MB | 缓存、消息队列 |
| Turso | SQLite | 500MB | 边缘数据库 |

#### B.20.5 云成本优化

```javascript
// 成本优化检查清单
const costOptimization = {
  compute: [
    '使用预留实例/承诺使用折扣',
    '自动扩展策略（按需扩容）',
    '使用 Spot/Preemptible 实例',
    '清理未使用的资源（闲置实例、未关联的存储卷）',
  ],
  storage: [
    '使用对象存储分层（热/冷/归档）',
    '启用生命周期管理自动迁移',
    '删除未使用的快照和备份',
    '压缩和优化存储数据',
  ],
  network: [
    '使用 CDN 减少源站流量',
    '启用数据压缩传输',
    '使用内网通信避免 NAT 费用',
    '合理配置负载均衡器',
  ],
  database: [
    '使用预留数据库实例',
    '启用自动暂停（无服务器数据库）',
    '定期清理历史数据',
    '使用只读副本分离读写',
  ],
};
```

---

### B.21 构建工具与包管理器

#### B.21.1 包管理器对比

| 工具 | 语言 | 特点 | 常用命令 |
|------|------|------|---------|
| npm | JavaScript | Node.js 自带 | npm install, npm run |
| Yarn | JavaScript | 更快、确定性安装 | yarn add, yarn start |
| pnpm | JavaScript | 磁盘效率高、严格 | pnpm add, pnpm dev |
| pip | Python | Python 官方 | pip install, pip list |
| Poetry | Python | 依赖管理+打包 | poetry add, poetry build |
| Cargo | Rust | Rust 官方 | cargo add, cargo build |
| Go Modules | Go | Go 官方 | go get, go mod tidy |
| Maven | Java | Java 标准 | mvn install, mvn test |
| Gradle | Kotlin DSL | 灵活构建 | gradle build |

#### B.21.2 npm/pnpm 包管理最佳实践

```json
// package.json 最佳实践
{
  "name": "@myorg/my-package",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "engines": {
    "node": ">=18.0.0",
    "pnpm": ">=8.0.0"
  },
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "test": "vitest run",
    "test:watch": "vitest",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/",
    "typecheck": "tsc --noEmit",
    "preview": "vite preview",
    "clean": "rm -rf dist/ .next/ node_modules/"
  },
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "typescript": "^5.3.0",
    "eslint": "^8.50.0",
    "prettier": "^3.0.0",
    "vitest": "^1.0.0"
  },
  "packageManager": "pnpm@8.15.0"
}
```

**包管理核心命令：**

```bash
# npm
npm init -y                    # 初始化项目
npm install <package>          # 安装包（生产依赖）
npm install -D <package>       # 安装包（开发依赖）
npm uninstall <package>        # 卸载包
npm update                     # 更新所有包
npm audit                      # 安全审计
npm audit fix                  # 修复安全漏洞
npm outdated                   # 查看过期包
npm ci                         # 根据 lockfile 精确安装

# pnpm（推荐）
pnpm add <package>             # 安装包
pnpm add -D <package>          # 安装开发依赖
pnpm remove <package>          # 卸载包
pnpm update                    # 更新包
pnpm audit                     # 安全审计
pnpm ls                        # 查看依赖树
pnpm why <package>             # 查看为什么依赖
```

#### B.21.3 构建工具配置

```javascript
// Vite 配置（现代前端构建）
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:4000',
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
        },
      },
    },
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/test/setup.ts',
  },
});
```

```javascript
// Webpack 配置（传统）
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: './src/index.tsx',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    clean: true,
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx'],
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',
    }),
  ],
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
      },
    },
  },
};
```

#### B.21.4 Monorepo 管理

```yaml
# pnpm-workspace.yaml
packages:
  - 'packages/*'
  - 'apps/*'
  - 'shared/*'
```

```
项目结构：
my-monorepo/
├── pnpm-workspace.yaml
├── package.json
├── packages/
│   ├── shared-utils/      # 共享工具库
│   │   ├── package.json
│   │   └── src/
│   ├── shared-types/      # 共享类型定义
│   │   ├── package.json
│   │   └── src/
│   └── ui-components/     # 共享 UI 组件
│       ├── package.json
│       └── src/
├── apps/
│   ├── web/               # Web 应用
│   │   ├── package.json
│   │   └── src/
│   ├── api/               # API 服务
│   │   ├── package.json
│   │   └── src/
│   └── mobile/            # 移动端
│       ├── package.json
│       └── src/
└── shared/
    └── config/            # 共享配置
        ├── eslint-config/
        ├── tsconfig/
        └── prettier-config/
```

**Turborepo 配置：**

```json
// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  },
  "globalDependencies": ["tsconfig.json"]
}
```

---

### B.22 代码审查最佳实践

#### B.22.1 代码审查清单

| 检查维度 | 检查项 | 说明 |
|---------|--------|------|
| 正确性 | 逻辑是否正确 | 代码是否实现了预期的功能 |
| 正确性 | 边界条件是否处理 | 空值、异常、极端输入 |
| 安全 | 输入是否验证 | SQL 注入、XSS、CSRF |
| 安全 | 敏感信息是否泄露 | API 密钥、密码、Token |
| 性能 | 是否有 N+1 查询 | 数据库查询效率 |
| 性能 | 是否有不必要的计算 | 缓存、记忆化 |
| 可维护 | 命名是否清晰 | 变量、函数、类名 |
| 可维护 | 函数是否过长 | 单一职责原则 |
| 可测试 | 是否容易测试 | 依赖注入、接口抽象 |
| 一致性 | 是否遵循项目规范 | 代码风格、架构模式 |

#### B.22.2 有效的代码审查

```markdown
## 代码审查注意事项

### 审查者（Reviewer）
1. **审查范围**：一次审查不超过 200-400 行代码
2. **审查顺序**：先理解整体设计，再看具体实现
3. **反馈方式**：问题式反馈而非命令式
   - ❌ "把这个函数拆开"
   - ✅ "这个函数似乎有多个职责，考虑是否应该拆分成更小的函数？"
4. **区分主次**：标注问题严重程度（blocker / major / minor / nit）
5. **肯定好的代码**：不要只提问题，也表扬好的设计

### 提交者（Author）
1. **PR 描述清晰**：说明改动原因、影响范围、测试情况
2. **PR 不要太**：一次 PR 解决一个问题
3. **回复所有评论**：表示接受或解释原因
4. **遇到分歧**：面对面讨论比评论更高效
5. **及时响应**：24小时内回复审查意见
```

**PR 模板示例：**

```markdown
## 描述
[简要描述这次改动的目的和内容]

## 关联 Issue
Closes #123

## 改动类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 重构
- [ ] 文档更新

## 测试
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] 手动测试完成

## 检查清单
- [ ] 代码遵循项目规范
- [ ] 没有引入新的安全风险
- [ ] 性能影响已评估
- [ ] 文档已更新（如需要）
- [ ] 添加了必要的测试

## 截图（如适用）
[UI 改动请附截图]
```

#### B.22.3 代码审查工具

| 工具 | 用途 | 特点 |
|------|------|------|
| GitHub PR Review | 代码审查 | 行内评论、审核流程 |
| GitLab Merge Request | 代码审查 | CI 集成、审批规则 |
| ESLint | 代码质量 | 静态分析、自动修复 |
| SonarQube | 代码质量平台 | 复杂度、重复代码、安全漏洞 |
| CodeRabbit | AI 代码审查 | 自动审查、智能建议 |
| Reviewdog | 自动评论 | 集成多种分析工具 |

---

### B.23 版本控制策略

#### B.23.1 Git 工作流对比

| 工作流 | 适用场景 | 优点 | 缺点 |
|--------|---------|------|------|
| GitHub Flow | 小型团队、持续部署 | 简单、快速迭代 | 无发布分支 |
| Git Flow | 大型项目、版本发布 | 层次清晰、适合发布 | 复杂、分支多 |
| Trunk-Based | CI/CD 成熟团队 | 极速迭代 | 需要高测试覆盖 |
| GitLab Flow | 环境分支管理 | 灵活、环境映射清晰 | 需要约定一致 |

**GitHub Flow（推荐小型项目）：**

```bash
# 1. 从 main 创建功能分支
git checkout -b feature/user-auth

# 2. 多轮提交
git add .
git commit -m "feat: add login form component"
git commit -m "feat: implement auth API integration"
git commit -m "test: add login form tests"

# 3. 推送到远程
git push -u origin feature/user-auth

# 4. 创建 Pull Request
# 5. 代码审查 → 合并到 main

# 6. 删除分支
git checkout main
git branch -d feature/user-auth
git push origin --delete feature/user-auth
```

#### B.23.2 提交信息规范（Conventional Commits）

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

| Type | 含义 | 示例 |
|------|------|------|
| feat | 新功能 | `feat(auth): add OAuth login` |
| fix | Bug 修复 | `fix(api): handle empty response` |
| docs | 文档 | `docs(readme): update installation guide` |
| refactor | 重构 | `refactor(utils): extract validation logic` |
| test | 测试 | `test(cart): add checkout tests` |
| chore | 杂务 | `chore(deps): update dependencies` |
| style | 样式 | `style(button): fix padding` |
| perf | 性能 | `perf(db): add index for user queries` |
| ci | CI/CD | `ci(actions): add deploy workflow` |

#### B.23.3 语义化版本（SemVer）

```
MAJOR.MINOR.PATCH

1.4.2
^    ^  ^
|    |  └── PATCH: Bug 修复（向下兼容）
|    └──── MINOR: 新功能（向下兼容）
└───────── MAJOR: 不兼容的 API 变更
```

**版本号规则：**
- **1.0.0**：正式发布
- **0.x.x**：开发阶段
- **x.y.z-alpha.1**：内测
- **x.y.z-beta.1**：公测
- **x.y.z-rc.1**：候选发布

---

### B.24 编程原则与哲学

#### B.24.1 SOLID 原则

| 原则 | 名称 | 描述 | 违反示例 | 正确做法 |
|------|------|------|---------|---------|
| S | 单一职责 | 一个类只有一个变更理由 | 一个类既处理业务逻辑又处理序列化 | 分离业务逻辑和序列化 |
| O | 开闭原则 | 对扩展开放，对修改关闭 | 添加新类型需要修改 switch 语句 | 使用策略模式或多态 |
| L | 里氏替换 | 子类可以替换父类 | 正方形继承长方形（违反数学关系） | 使用接口代替继承 |
| I | 接口隔离 | 接口应该小而专 | 一个"全能"接口 | 拆分多个特定接口 |
| D | 依赖倒置 | 依赖抽象而非具体实现 | 高层模块直接依赖低层模块 | 通过接口依赖 |

#### B.24.2 其他重要原则

| 原则 | 描述 | 示例 |
|------|------|------|
| DRY | 不要重复自己 | 提取公共代码为函数/模块 |
| KISS | 保持简单 | 不要过度设计，最简单的方案往往最好 |
| YAGNI | 你不会需要它 | 只实现当前需要的功能，不要预测未来需求 |
| Law of Demeter | 最少知识原则 | 不要链式调用的太深（如 a.b.c.d） |
| Composition over Inheritance | 组合优于继承 | 使用组合模式而非深层继承树 |

#### B.24.3 代码坏味道

| 坏味道 | 问题 | 解决方案 |
|--------|------|---------|
| 过长函数 | 函数做了太多事 | 拆分成小函数 |
| 过长参数列表 | 参数太多 | 封装为对象 |
| 重复代码 | 多处相同逻辑 | 提取公共函数 |
| 大型类 | 类职责太多 | 拆分成多个类 |
| 数据泥团 | 固定数据组合 | 创建值对象 |
| 过度耦合 | 类之间太依赖 | 引入接口解耦 |
| 注释太多 | 代码不清晰 | 重构使代码自文档化 |

---

### Vibe 练习

对 Claude Code 说：

> "我正在做一个 Web 项目，需要了解 API 密钥保护的最佳实践。请检查我的项目是否有敏感信息泄露风险，并告诉我还应该注意哪些安全问题。"

> "帮我分析这段代码的性能瓶颈，并提供具体的优化建议。"

> "帮我设计一个完整的监控方案，包括指标、日志和追踪，用于我的微服务架构。"

> "帮我为这个函数编写单元测试，覆盖所有边界条件。"

> "帮我审查这段代码，指出潜在的问题并提供改进建议。"

> "解释一下这段代码使用了什么设计模式，并建议是否有更好的替代方案。"

> "帮我设计一个可扩展的 API 架构，支持版本管理和向后兼容。"

> "帮我分析这个项目的依赖关系，检查是否有安全漏洞需要更新。"
