from fastapi import FastAPI
from app.api import api_router
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging
import time

from app.schemas import fail

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s| %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Light RAG Backend")
app.include_router(api_router, prefix="/api")
if __name__ =="__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    cost = round(time.time() - start_time, 4)
    client_ip = request.client.host if request.client else "unknown"
    logger.info(f"ip:{client_ip}|method:{request.method}|path:{request.url.path}|status:{response.status_code}|cost:{cost}s")
    return response



@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc:HTTPException):
    return fail(code=exc.status_code, msg=exc.detail)

@app.exception_handler(Exception)
async def global_exception_handler(request:Request, exc:Exception):
    logger.error(f"系统异常：{exc}")
    return fail(code=500, msg="服务器内部错误")


@app.exception_handler(StarletteHTTPException)
async def starlette_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return fail(code=exc.status_code, msg=exc.detail)
