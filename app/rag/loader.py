from fastapi import HTTPException


def load_document(file_path:str):
       try:
           if file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                      content = f.read()
                      return content
           else:
                      raise HTTPException(status_code=400, detail="不支持该文件类型，目前仅支持txt")
       except FileNotFoundError:
           raise HTTPException(status_code=404, detail="文件不存在")
       except UnicodeDecodeError:
           raise HTTPException(status_code=400, detail="文件编码不是utf-8")

def split_text(text:str, chunk_size:int=300, chunk_overlap:int=50):
    chunks=[]
    step = chunk_size-chunk_overlap
    start = 0
    while start<len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = start + step
    return chunks



