import streamlit as st
from reasoning_engine import multi_prompt_reasoning

st.set_page_config(page_title="Multi-Prompt Reasoning System", layout="centered")

st.title("🧠 Multi-Prompt Reasoning System (Free Version)")
st.write("Uses Hugging Face Inference API (No payment required)")

question = st.text_area("Enter your question", height=120)

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking step by step..."):
            answer = multi_prompt_reasoning(question)
        st.success("Final Answer")
        st.write(answer)
