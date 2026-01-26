"""
智能体基类 (Agent Base Class)
提供基础的智能体功能实现
"""

from typing import List, Optional
from .message import Message


class Agent:
    """智能体基类"""
    
    def __init__(self, name: str = "Agent"):
        """
        初始化智能体
        
        Args:
            name: 智能体名称
        """
        self.name = name
        self.history: List[Message] = []
        self.system_prompt = "你是一个有帮助的AI助手。"
    
    def set_system_prompt(self, prompt: str) -> None:
        """
        设置系统提示词
        
        Args:
            prompt: 系统提示词内容
        """
        self.system_prompt = prompt
    
    def add_message(self, message: Message) -> None:
        """
        添加消息到历史记录
        
        Args:
            message: 要添加的消息
        """
        self.history.append(message)
    
    def process(self, user_input: str) -> str:
        """
        处理用户输入并返回回复
        
        Args:
            user_input: 用户输入的内容
            
        Returns:
            智能体的回复
        """
        # 创建用户消息
        user_message = Message(role="user", content=user_input)
        self.add_message(user_message)
        
        # 生成回复 (这是一个简单的示例实现)
        response = self._generate_response(user_input)
        
        # 创建助手消息
        assistant_message = Message(role="assistant", content=response)
        self.add_message(assistant_message)
        
        return response
    
    def _generate_response(self, user_input: str) -> str:
        """
        生成响应 (内部方法，子类可以重写)
        
        Args:
            user_input: 用户输入
            
        Returns:
            生成的响应
        """
        # 这是一个简单的回显实现
        # 实际应用中，这里应该调用LLM API或其他AI服务
        return f"收到您的消息: {user_input}"
    
    def clear_history(self) -> None:
        """清除对话历史"""
        self.history.clear()
    
    def get_history(self) -> List[Message]:
        """
        获取对话历史
        
        Returns:
            消息历史列表
        """
        return self.history.copy()
    
    def __str__(self) -> str:
        return f"Agent(name='{self.name}', history_length={len(self.history)})"
