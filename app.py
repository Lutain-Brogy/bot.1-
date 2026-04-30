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
# Case instructions
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

   # Pains instructions

    elif "new pains" in clean_text:
        pain_input = st.text_input("Please paste your pains here:")

        if pain_input:
            import re

            pain_parts = re.split(r"[a-z]\.", pain_input.lower())

            cleaned_pains = []

            for pain in pain_parts:
                pain = pain.strip()

                if pain:
                    cleaned_pains.append(pain)

            st.session_state.pains = cleaned_pains

            st.write("Pains saved!")

    elif "my pains" in clean_text:
        if st.session_state.pains:
            st.write("Your pains:")

            for i, pain in enumerate(st.session_state.pains):
                st.write(f"{chr(65+i)}. {pain}")

        else:
            st.write("No pains saved yet.")

