from utils.langsmith_setup import *

import streamlit as st
from ui.research_page import show_research
from ui.chat_page import show_chat
from ui.my_companies_page import show_my_companies

st.set_page_config(
    page_title="Placement Prep Agent",
    layout="wide"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Research",
        "Chat",
        "My Companies"
    ]
)

if page == "Research":
    show_research()

elif page == "Chat":
    show_chat()

elif page == "My Companies":
    show_my_companies()