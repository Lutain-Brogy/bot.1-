import streamlit as st

st.title("AI Business Assistant")

if "case" not in st.session_state:
    st.session_state.case = None

user_input = st.text_input("You:")

if user_input:

    clean_text = user_input.lower()

    if "new case" in clean_text:
        st.session_state.case = "waiting"
        st.write("Cool, then please state your case.")

    elif st.session_state.case == "waiting":
        st.session_state.case = user_input
        st.write("Got it. I saved your case.")

    elif "my case" in clean_text or "show case" in clean_text:
        if st.session_state.case and st.session_state.case != "waiting":
            st.write(f"Your saved case is: {st.session_state.case}")
        else:
            st.write("You don’t have a saved case yet.")

    else:
        st.write("Hello, how can I help?")
