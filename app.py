import streamlit as st
import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

def initialize_chain():
    load_dotenv()
    #api_key = os.getenv('key')
    api_key=st.secrets["KEY"]
    model = "deepseek-r1-distill-llama-70b"
    deepseek = ChatGroq(api_key=api_key, model_name=model)

    parser = StrOutputParser()
    chain = deepseek | parser

    loader = TextLoader('data.txt', encoding='utf-8')
    data = loader.load()

    template = """
    You are an AI-powered chatbot designed to provide 
    information and assistance based on the context provided only.
    Don't in any way make things up.

    Context: {context}
    Question: {question}
    """
    return chain, data, template

def main():
    st.set_page_config(
        page_title="GianBot: Your AI Chat Companion",
        page_icon="🤖",  # You can use an emoji or a local file
        layout="centered"
    )
    
    # Give a fuller title or heading
    st.title("🤖 GianBot: Your AI Chat Companion")

    # Introduce your chatbot
    st.markdown(
        """
        [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github)](https://github.com/gminnocenti/GianMarcoInnocenti_DeepSeek_Personal_Chatbot)
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
    """
    **Welcome to GianBot!**  
    I'm an AI-powered chatbot built using the Deep Seek model, designed to help you uncover detailed and reliable information about Gian Marco Innocenti. Whether you're looking into his background, achievements, or insights into his work, I provide context-specific answers drawn from carefully curated data.

    ---
    """
)


    if "chain" not in st.session_state:
        st.session_state.chain, st.session_state.data, st.session_state.template = initialize_chain()

    # We’ll store chat history in st.session_state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display existing chat messages from history
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Capture new user input via st.chat_input
    user_input = st.chat_input("Type your question here...")

    if user_input:
        # 1. Append & display the user’s message first
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # 2. Generate the AI response
        prompt = st.session_state["template"].format(
            context=st.session_state["data"],
            question=user_input
        )
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                raw_answer = st.session_state["chain"].invoke(prompt)
            
            # Strip <think>...</think>
            answer_no_think = re.sub(r"<think>.*?</think>", "", raw_answer, flags=re.DOTALL).strip()
            st.write(answer_no_think)

        # 3. Append the assistant’s response to messages
        st.session_state["messages"].append({"role": "assistant", "content": answer_no_think})

if __name__ == "__main__":
    main()
