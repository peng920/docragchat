import os
import torch
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from chromadb.config import Settings
from langchain.vectorstores import Chroma

def get_vector_store():
    """获取或创建向量存储"""
    CHROMA_DB_DIR = "chroma_db"
    MODEL_PATH = "BAAI/bge-m3"
    LOCAL_MODEL_PATH = "/data/bge-m3"
    
    # 确保存储目录存在
    os.makedirs(CHROMA_DB_DIR, exist_ok=True)
    
    # 检查本地模型目录是否存在
    model_path = LOCAL_MODEL_PATH if os.path.exists(LOCAL_MODEL_PATH) else MODEL_PATH
    
    # 创建 Embeddings
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_kwargs = {"device": device}
    encode_kwargs = {"normalize_embeddings": True}  # Cosine Similarity


    embedding = HuggingFaceBgeEmbeddings(
        model_name=model_path,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
    )

    
    # 初始化 Chroma 向量存储
    vector_store = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embedding
    )
    
    return vector_store 