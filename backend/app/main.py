from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .services.document_service import DocumentService
from .services.qa_service import QAService
from .models import QuestionRequest

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

doc_service = DocumentService()
qa_service = QAService()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """上传并处理文档"""
    try:
        result = await doc_service.process_document(file)
        return {"message": "文档处理成功", "status": "success"}
    except Exception as e:
        return {"message": str(e), "status": "error"}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """处理问题并返回答案"""
    try:
        answer = await qa_service.get_answer(request.question)
        return {"answer": answer, "status": "success"}
    except Exception as e:
        return {"message": str(e), "status": "error"} 