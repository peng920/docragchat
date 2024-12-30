import os
from typing import List
from fastapi import UploadFile
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from ..utils.vector_store import get_vector_store

class DocumentService:
    async def process_document(self, file: UploadFile) -> bool:
        """处理上传的文档"""
        # 保存上传的文件
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        try:
            # 根据文件类型选择合适的加载器
            if file.filename.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            else:
                loader = TextLoader(file_path)
            
            # 加载文档
            documents = loader.load()
            
            # 分割文本
            text_splitter = CharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                separator="\n"
            )
            texts = text_splitter.split_documents(documents)
            
            # 将文档加入向量存储
            vector_store = get_vector_store()
            vector_store.add_documents(texts)
            
            return True
            
        finally:
            # 清理临时文件
            if os.path.exists(file_path):
                os.remove(file_path) 