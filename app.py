import streamlit as st
from transformers importpipeline
st.title("NLP Chatbot")

chatbot = pipeline("text-genertation",model="gpt2")

user_input = st.text_input("Ask me anything:")

if user_input:
    response = chatbot(user_input,max_length=00, num_return_sequence=1)[0]['generated_text']
    response = response.replace(user_input,""),strip()
    st.write(f"**Bot:**{response}")
    