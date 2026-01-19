# agent-myself

这是我自己初次学习如何搭建一个智能体

## 项目简介 (Project Introduction)

这是一个简单的智能体学习项目，实现了基础的智能体框架和对话系统。通过这个项目，你可以学习：

- 智能体的基本架构
- 消息处理和对话管理
- Python面向对象编程实践

## 项目结构 (Project Structure)

```
agent-myself/
├── agent_core/          # 核心模块
│   ├── __init__.py     # 模块初始化
│   ├── agent.py        # 智能体基类
│   └── message.py      # 消息类
├── examples/           # 使用示例
│   ├── basic_usage.py  # 基础使用示例
│   └── interactive_chat.py  # 交互式对话
├── requirements.txt    # 依赖包列表
└── README.md          # 项目文档
```

## 快速开始 (Quick Start)

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行基础示例

```bash
python examples/basic_usage.py
```

### 3. 运行交互式对话

```bash
python examples/interactive_chat.py
```

## 核心功能 (Core Features)

### Agent 类 (智能体基类)

主要功能：
- 管理对话历史
- 处理用户输入
- 生成响应
- 支持自定义系统提示词

```python
from agent_core import Agent

# 创建智能体
agent = Agent(name="我的助手")

# 设置系统提示词
agent.set_system_prompt("你是一个友好的助手")

# 处理消息
response = agent.process("你好！")
print(response)
```

### Message 类 (消息类)

表示智能体通信的消息，包含：
- role: 消息角色 (user/assistant/system)
- content: 消息内容
- timestamp: 时间戳

```python
from agent_core import Message

# 创建消息
msg = Message(role="user", content="你好")
print(msg)  # 输出: [user] 你好
```

## 使用示例 (Examples)

### 基础使用

```python
from agent_core import Agent

# 创建智能体
agent = Agent(name="学习助手")
agent.set_system_prompt("你是一个学习助手")

# 进行对话
response = agent.process("什么是人工智能？")
print(response)

# 查看历史
for msg in agent.get_history():
    print(msg)
```

### 交互式对话

运行 `examples/interactive_chat.py` 启动交互式对话界面。

支持的命令：
- `quit` 或 `exit`: 退出对话
- `clear`: 清除对话历史
- `history`: 查看对话历史

## 扩展方向 (Future Extensions)

这个基础框架可以扩展为：

1. **集成大语言模型 (LLM Integration)**
   - 接入 OpenAI API
   - 接入本地模型 (如 Ollama)

2. **增强功能 (Enhanced Features)**
   - 添加记忆管理
   - 实现工具调用
   - 支持多轮对话

3. **界面优化 (UI Improvements)**
   - Web界面
   - 命令行美化
   - 日志记录

## 学习资源 (Learning Resources)

- [LangChain 文档](https://python.langchain.com/)
- [OpenAI API 文档](https://platform.openai.com/docs)
- [Python 面向对象编程](https://docs.python.org/3/tutorial/classes.html)

## 贡献 (Contributing)

欢迎提交 Issue 和 Pull Request！

## 许可证 (License)

MIT License
