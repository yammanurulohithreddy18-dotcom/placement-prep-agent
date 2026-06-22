import streamlit as st
from utils.history import get_company_profiles


def show_my_companies():

    st.title("📚 My Researched Companies")

    history = get_company_profiles()

    if not history:
        st.info("No companies researched yet.")
        return

    company_records = []

    seen = set()

    for item in reversed(history):

        company = item["company"]

        if company.lower() in seen:
            continue

        seen.add(company.lower())

        company_records.append(item)

    st.write(
        f"You have researched {len(company_records)} companies:"
    )

    for item in company_records:

        company = item["company"]

        difficulty = item["difficulty"]
        rounds = item["rounds"]
        topics = item["topics"]
        tips = item["tips"]

        with st.expander(company):

            st.subheader("Difficulty")
            st.write(difficulty)

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Rounds")

                for r in rounds:
                    st.write(f"• {r}")

            with col2:

                st.subheader("Key Topics")

                for t in topics:
                    st.write(f"• {t}")

            st.subheader("Tips")

            for tip in tips:
                st.info(f"Focus heavily on: {tip}")

    st.subheader("Comparison Table")

    comparison_data = []

    for item in company_records:

        comparison_data.append({
            "Company": item["company"],
            "Difficulty": item["difficulty"],
            "Rounds": len(item["rounds"]),
            "Topics": len(item["topics"])
        })

    st.table(comparison_data)

    if st.button("Get AI Recommendation"):

        difficulty_rank = {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3
        }

        sorted_companies = sorted(
            comparison_data,
            key=lambda x: difficulty_rank.get(
                x["Difficulty"],
                2
            )
        )

        recommendation = ""

        for i, company in enumerate(
            sorted_companies,
            start=1
        ):
            recommendation += (
                f"{i}. "
                f"{company['Company']} "
                f"({company['Difficulty']})\n"
            )

        st.success(
            f"""
Recommended Preparation Order:

{recommendation}

Reason:

• Start with easier companies.
• Build confidence gradually.
• Move to medium-level interviews.
• Finish with the hardest companies.
            """
        )