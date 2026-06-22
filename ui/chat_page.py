import streamlit as st

from rag.retriever import retrieve_company_info
from agents.chat_agent import ask_company


def show_chat():

    st.title("💬 Chat with Your Agent")

    if "company" not in st.session_state:
        st.warning("Research a company first.")
        return

    company = st.session_state["company"]
    role = st.session_state["role"]

    st.subheader(
        f"Asking about: {company} - {role}"
    )

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    user_question = st.chat_input(
        "Ask anything about the interview process..."
    )

    if user_question:

        context = retrieve_company_info(company)

        answer = ask_company(
            company,
            role,
            context,
            user_question
        )

        st.session_state["chat_history"].append(
            ("user", user_question)
        )

        st.session_state["chat_history"].append(
            ("assistant", answer)
        )

    for role_name, message in st.session_state["chat_history"]:

        with st.chat_message(role_name):
            st.markdown(message)