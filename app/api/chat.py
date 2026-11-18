from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.vector_store import search_text
from app.rag.llm import get_answer
from app.schemas import success, fail

router = APIRouter()
class ChatRequest(BaseModel):
    query:str

@router.post("/chat")
async def chat(req: ChatRequest):
    print("==== 进入chat接口，query：", req.query)
    query = req.query
    context = search_text(query)
    if not context:
        return fail(msg="知识库未查询到相关内容")
    ans = await get_answer(query, context)
    return success(data={"answer": ans})

