import streamlit as st
import requests
import json

# 配置页面
st.set_page_config(page_title="文档问答系统", layout="wide")

# 设置API地址
API_URL = "http://localhost:8000"

def upload_file(file):
    """上传文件到后端"""
    files = {"file": file}
    response = requests.post(f"{API_URL}/upload", files=files)
    return response.json()

def ask_question(question):
    """发送问题到后端"""
    response = requests.post(
        f"{API_URL}/ask",
        json={"question": question}
    )
    return response.json()

def main():
    st.title("智能文档问答系统")
    
    # 文件上传部分
    st.header("文档上传")
    uploaded_file = st.file_uploader("选择要上传的文档", type=["pdf", "txt"])
    
    if uploaded_file is not None:
        if st.button("处理文档"):
            with st.spinner("正在处理文档..."):
                result = upload_file(uploaded_file)
                if result["status"] == "success":
                    st.success("文档处理成功！")
                else:
                    st.error(f"处理失败：{result['message']}")
    
    # 问答部分
    st.header("文档问答")
    question = st.text_input("请输入您的问题：")
    
    if st.button("提交问题"):
        if question:
            with st.spinner("正在思考..."):
                result = ask_question(question)
                if result.get("status") == "success":
                    st.write("答案：", result["answer"])
                else:
                    st.error(f"获取答案失败：{result.get('message')}")
        else:
            st.warning("请输入问题！")

if __name__ == "__main__":
    main() 