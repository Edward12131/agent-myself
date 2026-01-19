"""
交互式对话示例 (Interactive Chat Example)
创建一个交互式的对话界面
"""

import sys
import os

# 添加父目录到路径以便导入agent_core模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent_core import Agent


def main():
    """主函数"""
    print("=" * 50)
    print("智能体交互式对话 (Interactive Agent Chat)")
    print("=" * 50)
    print("输入 'quit' 或 'exit' 退出对话")
    print("输入 'clear' 清除对话历史")
    print("输入 'history' 查看对话历史")
    print("=" * 50)
    print()
    
    # 创建智能体实例
    agent = Agent(name="对话助手")
    agent.set_system_prompt("你是一个智能对话助手。")
    
    while True:
        try:
            # 获取用户输入
            user_input = input("您: ").strip()
            
            if not user_input:
                continue
            
            # 检查特殊命令
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("再见！")
                break
            
            elif user_input.lower() == 'clear':
                agent.clear_history()
                print("✓ 对话历史已清除")
                continue
            
            elif user_input.lower() == 'history':
                if not agent.get_history():
                    print("(对话历史为空)")
                else:
                    print("\n对话历史:")
                    print("-" * 40)
                    for i, msg in enumerate(agent.get_history(), 1):
                        print(f"{i}. {msg}")
                    print("-" * 40)
                continue
            
            # 处理正常对话
            response = agent.process(user_input)
            print(f"助手: {response}")
            print()
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"错误: {e}")


if __name__ == "__main__":
    main()
