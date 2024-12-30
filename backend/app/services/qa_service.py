from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from ..utils.vector_store import get_vector_store
from dotenv import load_dotenv
import os

load_dotenv()

class QAService:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.95,
            model=os.getenv('MODEL_NAME'),
            openai_api_key=os.getenv('OPENAI_API_KEY'), #your api key
            openai_api_base=os.getenv('OPENAI_API_URL')
        )
        self.vector_store = get_vector_store()
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vector_store.as_retriever(),
            return_source_documents=True
        )
        
    async def get_answer(self, question: str) -> str:
        """获取问题的答案"""
        chat_history = []  # 这里可以扩展支持聊天历史
        result = self.qa_chain({"question": question, "chat_history": chat_history})
        return result["answer"] 