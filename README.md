# Light-RAG-Backend
轻量RAG后端，FastAPI实现，支持文档上传、向量检索、流式问答

## 技术栈
- Python + FastAPI
- ChromaDB 向量库
- Pydantic 数据校验
- httpx 异步调用大模型API

## 功能
✅ 文档上传
✅ 文档向量化入库
✅ 检索增强问答
✅ SSE流式输出

## 启动
1. 安装依赖
pip install -r requirements.txt

2. 复制 .env.example 为 .env，填入大模型KEY

3. 启动服务
uvicorn main:app --reload

访问：http://127.0.0.1:8000/docs
