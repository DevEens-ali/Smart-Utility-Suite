import streamlit as st

from config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)

from assets.style import apply_custom_css
from components.sidebar import render_sidebar
from components.home import render_home


def main():

    # Must be the first Streamlit command
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
    )

    # Apply custom CSS
    apply_custom_css()

    # Render Sidebar
    selected_page = render_sidebar()

    # Render Home Page
    render_home()


if __name__ == "__main__":
    main()