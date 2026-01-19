"""
安装配置文件 (Setup Configuration)
"""

from setuptools import setup, find_packages

setup(
    name="agent-myself",
    version="0.1.0",
    description="一个简单的智能体学习项目 (A simple agent learning project)",
    author="Edward12131",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "python-dotenv>=1.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
