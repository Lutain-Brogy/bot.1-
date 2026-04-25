import streamlit as st

st.title("My AI Chatbot UI")

user_input = st.text_input("You:")

if user_input:

    # simple if/else brain
    if user_input.lower() == "hello":
        st.write("Bot: Hello! 👋")

    elif user_input.lower() == "how are you":
        st.write("Bot: I'm good! How can I help you?")

    elif user_input.lower() == "bye":
        st.write("Bot: Goodbye! 👋")

    else:
        st.write("Bot: I don't understand that yet.")
