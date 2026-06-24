import os
from utils.langsmith_setup import *

import streamlit as st
from ui.research_page import show_research
from ui.chat_page import show_chat
from ui.my_companies_page import show_my_companies
import sentry_sdk

# =========================
# SENTRY
# =========================

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    send_default_pii=True,
    traces_sample_rate=1.0,
)

sentry_sdk.capture_message("Sentry is connected")

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Placement Prep Agent",
    layout="wide"
)

# =========================
# PASSWORD PROTECTION
# =========================

def check_password():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:

        st.title("🔒 Placement Prep Agent")

        password = st.text_input(
            "Enter Password",
            type="password"
        )

        if st.button("Login"):

            correct_password = os.getenv("APP_PASSWORD")

            if not correct_password:
                st.error("APP_PASSWORD not configured.")
                st.stop()

            if password == correct_password:
                st.session_state.authenticated = True
                st.rerun()

            else:
                st.error("❌ Incorrect password")

        st.stop()


check_password()

# =========================
# NAVIGATION
# =========================

page = st.sidebar.radio(
    "Navigation",
    [
        "Research",
        "Chat",
        "My Companies"
    ]
)

# =========================
# PAGES
# =========================

if page == "Research":
    show_research()

elif page == "Chat":
    show_chat()

elif page == "My Companies":
    show_my_companies()