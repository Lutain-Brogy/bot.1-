import streamlit as st

st.title("AI Business Assistant")

user_input = st.text_input("You:")
text = "Hi there, I have a new case"

clean_text = text.lower()

if "new case" in clean_text:
    print("Cool, proceed by stating your case.")
else:
    print("Hello how can I help?")
