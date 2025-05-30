import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit UI configuration
st.set_page_config(
    page_title="Gemini 1.5 Flash Chat",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("💬 Gemini 1.5 Flash Chat")
st.caption("Chat with Google's Gemini 1.5 Flash model")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("메시지를 입력하세요..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Gemini's response
    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):
            try:
                response = model.generate_content(prompt)
                response_text = response.text
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"오류가 발생했습니다: {str(e)}")

# Add sidebar information
with st.sidebar:
    st.title("ℹ️ 정보")
    st.markdown("""
    ### Gemini 1.5 Flash
    - Google의 최신 AI 모델
    - 빠른 응답 속도
    - 자연스러운 대화 가능
    
    ### 사용 방법
    1. 메시지 입력창에 질문을 입력하세요
    2. Enter 키를 누르면 AI가 응답합니다
    3. 대화 내용은 자동으로 저장됩니다
    """) 