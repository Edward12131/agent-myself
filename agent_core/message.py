"""
消息类 (Message Class)
用于处理智能体的输入输出消息
"""

from typing import Optional
from datetime import datetime


class Message:
    """表示智能体通信的消息"""
    
    def __init__(self, role: str, content: str, timestamp: Optional[datetime] = None):
        """
        初始化消息
        
        Args:
            role: 消息角色 (user, assistant, system)
            content: 消息内容
            timestamp: 消息时间戳
        """
        self.role = role
        self.content = content
        self.timestamp = timestamp or datetime.now()
    
    def __str__(self) -> str:
        return f"[{self.role}] {self.content}"
    
    def __repr__(self) -> str:
        return f"Message(role='{self.role}', content='{self.content[:20]}...', timestamp={self.timestamp})"
    
    def to_dict(self) -> dict:
        """转换为字典格式"""
        return {
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp.isoformat()
        }
