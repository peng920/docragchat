# 智能文档问答系统

这是一个基于个人文档的智能问答系统，支持文档上传、向量化存储和智能问答功能。

## 功能特点

- 支持PDF和TXT文档上传
- 使用Chroma进行向量存储
- 基于OpenAI API进行智能问答
- 简洁的Web界面

## 安装说明

1. 克隆项目到本地
2. 安装后端依赖：
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. 安装前端依赖：
   ```bash
   cd frontend
   pip install -r requirements.txt
   ```

## 环境配置

创建.env文件并配置以下环境变量： 
`OPENAI_API_KEY=你的OpenAI API密钥`

## 运行说明

1. 启动后端服务：
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. 启动前端服务：
   ```bash
   cd frontend
   streamlit run app.py
   ```

## 使用说明

1. 打开浏览器访问 http://localhost:8501
2. 上传文档并等待处理完成
3. 在问答界面输入问题并获取答案

需要进行进一步的扩展和优化：
- 添加用户认证
- 支持更多文档格式
- 优化文档分块策略
- 添加多轮对话支持
- 优化向量检索策略
- 添加文档管理功能
