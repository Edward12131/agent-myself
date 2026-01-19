"""
基础使用示例 (Basic Usage Example)
演示如何创建和使用简单的智能体
"""

import sys
import os

# 添加父目录到路径以便导入agent_core模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent_core import Agent, Message


def main():
    """主函数"""
    print("=" * 50)
    print("智能体基础示例 (Basic Agent Example)")
    print("=" * 50)
    print()
    
    # 创建智能体实例
    agent = Agent(name="学习助手")
    print(f"✓ 创建智能体: {agent}")
    print()
    
    # 设置系统提示词
    agent.set_system_prompt("你是一个友好的学习助手，帮助用户理解和学习新知识。")
    print(f"✓ 设置系统提示词")
    print()
    
    # 模拟对话
    test_inputs = [
        "你好！",
        "什么是人工智能？",
        "谢谢你的解释！"
    ]
    
    print("开始对话:")
    print("-" * 50)
    
    for user_input in test_inputs:
        print(f"\n用户: {user_input}")
        response = agent.process(user_input)
        print(f"助手: {response}")
    
    print("\n" + "-" * 50)
    print()
    
    # 显示对话历史
    print("对话历史:")
    print("-" * 50)
    for i, message in enumerate(agent.get_history(), 1):
        print(f"{i}. {message}")
    
    print("\n" + "=" * 50)
    print(f"✓ 示例运行完成！共 {len(agent.get_history())} 条消息")
    print("=" * 50)


if __name__ == "__main__":
    main()
