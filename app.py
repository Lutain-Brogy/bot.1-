import streamlit as st

st.title("AI Business Assistant")

user_input = st.text_input("You:")

# 🧠 MEMORY (session state first)
if "case" not in st.session_state:
    st.session_state.case = ""

if "pains" not in st.session_state:
    st.session_state.pains = []

if "factors" not in st.session_state:
    st.session_state.factors = []

if "corrections" not in st.session_state:
    st.session_state.corrections = []

if "plan" not in st.session_state:
    st.session_state.plan = ""

if "final_corrections" not in st.session_state:
    st.session_state.final_corrections = []

# 🧠 INPUT GATE
if user_input:
    clean_text = user_input.lower()

    if "new case" in clean_text:
        new_case = st.text_input("Please paste your case:")

        if new_case:
            st.session_state.case = new_case
            st.write("Saved!")

    elif "my case" in clean_text:
        if st.session_state.case:
            st.write("Your case:", st.session_state.case)

        else:
            st.write("No case saved yet.")

