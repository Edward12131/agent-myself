"""
自定义智能体示例 (Custom Agent Example)
演示如何继承和扩展基础智能体类
"""

import sys
import os

# 添加父目录到路径以便导入agent_core模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent_core import Agent


class EchoAgent(Agent):
    """简单的回声智能体，会重复用户说的话"""
    
    def _generate_response(self, user_input: str) -> str:
        """重写响应生成方法"""
        return f"🔊 回声: {user_input}"


class CounterAgent(Agent):
    """计数智能体，记录处理的消息数量"""
    
    def __init__(self, name: str = "CounterAgent"):
        super().__init__(name)
        self.message_count = 0
    
    def process(self, user_input: str) -> str:
        """重写process方法，添加计数功能"""
        self.message_count += 1
        response = super().process(user_input)
        return response
    
    def _generate_response(self, user_input: str) -> str:
        """生成包含计数的响应"""
        return f"[消息 #{self.message_count}] 收到: {user_input}"


class PoliteAgent(Agent):
    """礼貌的智能体，总是使用礼貌用语"""
    
    def _generate_response(self, user_input: str) -> str:
        """生成礼貌的响应"""
        responses = [
            f"您好！您说: '{user_input}'",
            f"谢谢您的消息！您提到: '{user_input}'",
            f"很高兴为您服务！关于 '{user_input}'，我已收到。",
        ]
        # 根据消息长度选择响应
        index = len(self.history) % len(responses)
        return responses[index]


def main():
    """主函数"""
    print("=" * 60)
    print("自定义智能体示例 (Custom Agent Examples)")
    print("=" * 60)
    print()
    
    # 测试回声智能体
    print("1. 回声智能体 (Echo Agent)")
    print("-" * 60)
    echo = EchoAgent(name="回声助手")
    for msg in ["你好", "测试", "再见"]:
        print(f"  用户: {msg}")
        print(f"  助手: {echo.process(msg)}")
    print()
    
    # 测试计数智能体
    print("2. 计数智能体 (Counter Agent)")
    print("-" * 60)
    counter = CounterAgent(name="计数助手")
    for msg in ["第一条", "第二条", "第三条"]:
        print(f"  用户: {msg}")
        print(f"  助手: {counter.process(msg)}")
    print(f"  ℹ️  总消息数: {counter.message_count}")
    print()
    
    # 测试礼貌智能体
    print("3. 礼貌智能体 (Polite Agent)")
    print("-" * 60)
    polite = PoliteAgent(name="礼貌助手")
    for msg in ["早上好", "帮个忙", "谢谢"]:
        print(f"  用户: {msg}")
        print(f"  助手: {polite.process(msg)}")
    print()
    
    print("=" * 60)
    print("✓ 所有自定义智能体示例运行完成！")
    print("=" * 60)
    print()
    print("提示: 你可以通过继承 Agent 类并重写 _generate_response 方法")
    print("      来创建具有自定义行为的智能体。")


if __name__ == "__main__":
    main()
