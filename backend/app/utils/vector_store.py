import os
from langchain.embeddings import OpenAIEmbeddings
from chromadb.config import Settings
from langchain.vectorstores import Chroma

def get_vector_store():
    """获取或创建向量存储"""
    CHROMA_DB_DIR = "chroma_db"
    
    # 确保存储目录存在
    os.makedirs(CHROMA_DB_DIR, exist_ok=True)
    
    # 创建 OpenAI Embeddings
    embeddings = OpenAIEmbeddings()
    
    # 初始化 Chroma 向量存储
    vector_store = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings
    )
    
    return vector_store 