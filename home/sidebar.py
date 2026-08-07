"""
Pure Streamlit Sidebar

No external libraries.
Easy to understand.
Easy to extend.
"""

import streamlit as st

from config.menu_config import HOME_ITEM, MENU_SECTIONS


def render_sidebar():
    """
    Render the sidebar and return the selected page.
    """

    with st.sidebar:

        st.title("🧮 UtilityHub")

        st.divider()

        # ---------------- Home ---------------- #

        if st.button(
            HOME_ITEM["label"],
            use_container_width=True,
            key="home",
        ):
            st.session_state.page = HOME_ITEM["label"]

        st.write("")

        # ---------------- Sections ---------------- #

        for section in MENU_SECTIONS:

            st.subheader(section["title"])

            for item in section["items"]:

                if st.button(
                    item["label"],
                    use_container_width=True,
                    key=item["label"],
                ):
                    st.session_state.page = item["label"]

            st.write("")

    if "page" not in st.session_state:
        st.session_state.page = HOME_ITEM["label"]

    return st.session_state.page