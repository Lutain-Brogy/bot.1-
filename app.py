import streamlit as st

st.title("AI Business Assistant")

# memory setup
if "step" not in st.session_state:
    st.session_state.step = None

if "case" not in st.session_state:
    st.session_state.case = None

if "pains" not in st.session_state:
    st.session_state.pains = []

user_input = st.text_input("You:")

if user_input:

    clean_text = user_input.lower()

    # STEP 1: start case
    if "new case" in clean_text:
        st.session_state.step = "waiting_case"
        st.session_state.pains = []  # reset pains
        st.write("Cool, please state your case.")

    # STEP 2: save case
    elif st.session_state.step == "waiting_case":
        st.session_state.case = user_input
        st.session_state.step = "waiting_pains"

        st.write(f"Your saved case is: {st.session_state.case}")
        st.write("Please give your pains:")
        st.write("A.")
        st.write("B.")

    # STEP 3: collect pains
    elif st.session_state.step == "waiting_pains":

        st.session_state.pains.append(user_input)
        st.write(f"- {user_input}")

        if len(st.session_state.pains) == 2:
            st.write("Pains saved successfully.")
            st.session_state.step = "done"

    # STEP 4: show pains anytime
    elif "show pains" in clean_text or "my pains" in clean_text:

        if st.session_state.pains:
            st.write("Here are your pains:")
            for p in st.session_state.pains:
                st.write(f"- {p}")
        else:
            st.write("No pains saved yet.")

    else:
        st.write("Hello, how can I help?")
