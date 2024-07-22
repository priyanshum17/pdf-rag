import streamlit as st

st.title("Chat With Your PDF & CSV")

uploaded_file = st.file_uploader("Upload PDF or CSV", type=["pdf", "csv"])

st.chat_input("Type your message here...")
