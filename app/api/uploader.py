from fastapi import APIRouter, UploadFile, File, HTTPException
import os, uuid
from app.config import settings
from app.rag.loader import load_document, split_text
from app.rag.vector_store import add_texts
from app.schemas import success, fail
router = APIRouter()
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.size and file.size>settings.max_file_size:
        return fail(code=413, msg="文件过大")
    file_id = str(uuid.uuid4())
    if not file.filename:
        return fail(code=400, msg="文件名不能为空")
    suffix = os.path.splitext(file.filename)[1]
    save_name = file_id + suffix
    save_path = os.path.join(settings.upload_dir, save_name)
    os.makedirs(settings.upload_dir, exist_ok=True)
    with open(save_path, "wb") as f:
        content = await file.read()
        f.write(content)
    text = load_document(save_path)
    chunks = split_text(text)
    add_texts(chunks, file_id)

    return success(msg="上传成功", data = {"file_id":file_id})



