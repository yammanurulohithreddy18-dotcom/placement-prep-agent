import streamlit as st

from workflow import company_workflow, feedback_workflow

from utils.history import (
    save_attempt,
    save_company_profile,
    get_company_profile
)

from utils.usage_tracker import (
    check_token_limit,
    get_tokens_used,
    get_remaining_tokens,
    get_cost
)


def show_research():

    st.title("Research a Company")

    # Usage Dashboard
    st.sidebar.markdown("## 📊 Usage Dashboard")
    st.sidebar.write(f"Tokens Used Today: {get_tokens_used()}")
    st.sidebar.write(f"Remaining Tokens: {get_remaining_tokens()}")
    st.sidebar.write(f"Estimated Cost: ${get_cost()}")
    st.sidebar.write("Daily Limit: 1000 Tokens")

    company = st.text_input("Company Name")
    role = st.text_input("Role")

    if st.button("Research"):

        estimated_tokens = 500

        if not check_token_limit(estimated_tokens):
            st.error(
                "🚫 Token limit reached. Daily limit is 1000 tokens. Please try again tomorrow."
            )
            st.stop()

        existing_profile = get_company_profile(company)

        if existing_profile:
            st.info("⚡ Loaded from Company Cache")

        result = company_workflow(company, role)

        profile = result["profile"]
        questions = result["questions"]

        st.session_state["company"] = company
        st.session_state["role"] = role
        st.session_state["profile"] = profile
        st.session_state["questions"] = questions

        save_company_profile(profile)

        save_attempt(
            company,
            role,
            "Research Completed",
            0
        )

    if "profile" not in st.session_state:
        return

    profile = st.session_state["profile"]
    questions = st.session_state["questions"]

    st.success("Research complete!")

    st.header(
        f"{profile.company_name} - {st.session_state['role']} Profile"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Difficulty",
            profile.difficulty
        )

    with col2:
        st.metric(
            "Interview Rounds",
            len(profile.interview_rounds)
        )

    with col3:
        st.metric(
            "Key Topics",
            len(profile.key_topics)
        )

    st.subheader("Interview Rounds")

    for i, round_name in enumerate(
        profile.interview_rounds,
        start=1
    ):
        st.write(f"{i}. {round_name}")

    st.subheader("Preparation Tips")

    for topic in profile.key_topics[:3]:
        st.info(
            f"Focus heavily on: {topic}"
        )

    st.subheader("Key Topics")

    for topic in profile.key_topics:
        st.write(f"• {topic}")

    st.subheader("Interview Questions")

    for i, question in enumerate(
        questions.questions[:5],
        start=1
    ):
        st.write(f"### {i}.")
        st.write(question)

    st.divider()

    st.header("Answer Evaluation")

    selected_question = st.selectbox(
        "Select Question",
        questions.questions
    )

    answer = st.text_area(
        "Your Answer",
        height=200
    )

    if st.button("Evaluate Answer"):

        if not answer.strip():
            st.warning(
                "Please enter an answer."
            )
            return

        feedback = feedback_workflow(
            selected_question,
            answer
        )

        save_attempt(
            st.session_state["company"],
            st.session_state["role"],
            selected_question,
            feedback.score
        )

        st.success(
            f"Score: {feedback.score}"
        )

        st.subheader("Strengths")

        for item in feedback.strengths:
            st.write(f"✅ {item}")

        st.subheader("Improvements")

        for item in feedback.improvements:
            st.write(f"🔹 {item}")