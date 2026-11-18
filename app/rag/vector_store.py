import chromadb
import dashscope
from dashscope import TextEmbedding
from app.config import settings


def get_collection():
    client = chromadb.PersistentClient(path=settings.chroma_persist_path)
    coll = client.get_or_create_collection(
        name="rag_collection",
        embedding_function=None
    )
    return coll

def add_texts(texts:list[str], file_id:str):
    collection = get_collection()
    embeddings = []
    for text in texts:
        vec = get_embedding(text)
        embeddings.append(vec)
    ids = [f"{file_id}_{i}"for i in range(len(texts))]
    collection.add(
        documents = texts,
        embeddings = embeddings,
        ids = ids
    )

def search_text(query: str, top_k: int = 3):
    collection = get_collection()
    query_vec = get_embedding(query)
    res = collection.query(
        query_embeddings=[query_vec],
        n_results=top_k
    )
    docs = res["documents"]
    if docs is None:
        return []
    return docs[0]

def get_embedding(text: str):
    api_key = settings.embedding_api_key
    print("DEBUG api_key:", repr(api_key))
    resp = TextEmbedding.call(
        api_key=api_key,
        model=settings.embedding_model,
        input=[text]
    )
    if resp.status_code == 200:
        embedding = resp.output["embeddings"][0]["embedding"]
        return embedding
    else:
        raise Exception(f"embedding接口调用失败，code:{resp.code}, msg:{resp.message}")

