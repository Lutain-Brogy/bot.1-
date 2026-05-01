import streamlit as st

st.title("AI Business Assistant")

user_input = st.text_input("You:")


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

if "steps" not in st.session_state:
    st.session_state.steps = ""

if "final_plan" not in st.session_state:
    st.session_state.final_plan = ""

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
if user_input:
    clean_text = user_input.lower()
    
    if "new pains" in clean_text:
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
  # Factors instructions
if user_input:
    clean_text = user_input.lower()

    if "new factors" in clean_text:
        factor_input = st.text_input("Please paste your factors here:")

        if factor_input:
            import re

            factor_parts = re.split(r"a\d+", factor_input.lower())

            cleaned_factors = []

            for f in factor_parts:
                f = f.strip()

                if f:
                    cleaned_factors.append(f)

            st.session_state.factors = cleaned_factors

            st.write("Factors saved!")

    elif "my factors" in clean_text:
        if st.session_state.factors:
            st.write("Your factors:")

            for i, factor in enumerate(st.session_state.factors):
                st.write(f"a{i+1}. {factor}")

        else:
            st.write("No factors saved yet.")

# Corrections instructions
if user_input:
    clean_text = user_input.lower()

    if "new corrections" in clean_text:
        correction_input = st.text_input("Please paste your corrections here:")

        if correction_input:
            import re

            correction_parts = re.split(r"b\d+", correction_input.lower())

            cleaned_corrections = []

            for c in correction_parts:
                c = c.strip()

                if c:
                    cleaned_corrections.append(c)

            st.session_state.corrections = cleaned_corrections

            st.write("Corrections saved!")

    elif "my corrections" in clean_text:
        if st.session_state.corrections:
            st.write("Your corrections:")

            for i, c in enumerate(st.session_state.corrections):
                st.write(f"b{i+1}. {c}")

        else:
            st.write("No corrections saved yet.")



#plan instructions
if user_input:
    clean_text = user_input.lower()

    if "plan" in clean_text:
        plan_input = st.text_input("Please write your plan:")

        if plan_input:
            st.session_state.plan = plan_input
            st.write("Plan saved!")

        # SHOW PLAN
        if st.session_state.plan:
            st.write("📌 PLAN:")
            st.write(st.session_state.plan)

            # SHOW CORRECTIONS BELOW
            st.write("📎 CORRECTIONS:")

            if st.session_state.corrections:
                for i, c in enumerate(st.session_state.corrections):
                    st.write(f"b{i+1}. {c}")
            else:
                st.write("No corrections saved yet.")
# final correstions
if user_input:
    clean_text = user_input.lower()

    if "final corrections" in clean_text:
        correction_input = st.text_input("Please paste your corrections here:")

        if correction_input:
            import re

            correction_parts = re.split(r"c\d+", correction_input.lower())

            cleaned_corrections = []

            for c in correction_parts:
                c = c.strip()

                if c:
                    cleaned_corrections.append(c)

            st.session_state.final_corrections = cleaned_corrections

            st.write("Corrections saved!")

    elif "my final corrections" in clean_text:
        if st.session_state.final_corrections:
            st.write("Your corrections:")

            for i, c in enumerate(st.session_state.final_corrections):
                st.write(f"c{i+1}. {c}")

        else:
            st.write("No corrections saved yet.")


    # Steps instructions
if user_input:
    clean_text = user_input.lower()

    if "my steps" in clean_text:
        if st.session_state.steps:
            st.write("Your steps:", st.session_state.steps)
        else:
            st.write("No steps saved yet.")

    elif "new steps" in clean_text:
        step_input = st.text_input("Please paste your steps:")

        if step_input:
            st.session_state.steps = step_input
            st.write("Saved!")


