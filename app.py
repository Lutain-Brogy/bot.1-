import streamlit as st

st.title("My AI Chatbot UI")

user_input = st.text_input("You:")

if user_input:

    text = user_input.lower()

    # simple chatbot responses
    if text == "hello":
        st.write("Bot: Hello! 👋")

    elif text == "how are you":
        st.write("Bot: I'm good! How can I help you?")

    elif text == "bye":
        st.write("Bot: Goodbye! 👋")

    elif text == "new case":
        st.write("Bot: Enter in format:")
        st.write("A. Case name")
        st.write("B. Goal")

        data = st.text_area("Paste A and B here:")

        if data:
            parts = data.split("\n")

            case = parts[0].replace("A.", "").strip()
            goal = parts[1].replace("B.", "").strip()

            st.write("Saved Case:")
            st.write("Case:", case)
            st.write("Goal:", goal)

    else:
        st.write("Bot: I don't understand that yet.")
