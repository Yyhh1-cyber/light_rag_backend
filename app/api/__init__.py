from fastapi import APIRouter
from app.api.uploader import router as uploader_router
from app.api.chat import router as chat_router

api_router = APIRouter()
api_router.include_router(uploader_router, tags=["文件上传"])
api_router.include_router(chat_router, tags=["问答对话"])
