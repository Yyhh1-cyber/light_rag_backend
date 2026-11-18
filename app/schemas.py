from pydantic import BaseModel
from typing import Optional, Any
from fastapi.responses import JSONResponse


class Resp(BaseModel):
    code:int
    msg:str
    data:Optional[Any] = None

def success(msg:str = "操作成功", data: Any = None) -> JSONResponse:
    return JSONResponse(
        content={
            "code": 200,
            "msg": msg,
            "data": data
        }
    )
def fail(code:int, msg:str, data:Any = None) -> JSONResponse:
    return JSONResponse(
        content={
            "code":code,
            "msg": msg,
            "data": data
        }
    )