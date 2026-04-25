import streamlit as st

st.title("My AI Chatbot UI")

user_input = st.text_input("You:")

if user_input:
    st.write("Bot: You said ->", user_input)
