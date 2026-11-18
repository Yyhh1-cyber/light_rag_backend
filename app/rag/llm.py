import httpx
from fastapi import HTTPException

from app.config import settings

async def get_answer(query: str, context:list[str]):
    context_text = "\n".join(context)
    prompt = f"""你只能根据下面给到的参考资料回答问题，不知道就说没有相关信息。
    参考资料:
    {context_text}
    
    用户问题:{query}
    """
    headers = {
        "Authorization": f"Bearer {settings.llm_api_key}",
        "Content-Type":"application/json"
    }
    payload = {
        "model": settings.llm_model,
        "messages" : [
            {"role":"user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            url=settings.llm_base_url,
            headers=headers,
            json=payload
        )
        print("状态码：", resp.status_code)
        print("原始返回内容：", resp.text)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)

        data = resp.json()
    answer = data["choices"][0]["message"]["content"]
    return answer

