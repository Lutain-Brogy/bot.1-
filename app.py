import streamlit as st

st.title("AI Business Assistant")

user_input = st.text_input("You:")

if user_input:
    clean_text = user_input.lower()

    if "new case" in clean_text:
        st.write("Cool, proceed by stating your case.")
    else:
        st.write("Hello how can I help?")
