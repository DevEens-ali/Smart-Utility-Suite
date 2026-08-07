"""
Home page UI component.

Only visual content lives here - no calculator logic is implemented yet,
per current project scope.
"""

import streamlit as st
from config.settings import APP_NAME


def _render_top_header() -> None:
    """Top-right theme toggle icon (decorative only for now)."""
    col_spacer, col_icon = st.columns([20, 1])
    with col_icon:
        st.markdown(
            '<div class="top-header-row"><i class="bi bi-sun" '
            'style="font-size:1.3rem;color:#374151;"></i></div>',
            unsafe_allow_html=True,
        )


def _render_page_title() -> None:
    st.markdown(
        f'<div class="page-title">Welcome to <span>{APP_NAME}</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="page-subtitle">All the tools you need in one place.</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)


def _render_hero() -> None:
    """Centered calculator icon, heading, and helper text."""
    st.markdown(
        """
        <div class="hero-icon-box">
            <i class="bi bi-calculator"></i>
        </div>
        <div class="hero-title">Your All-in-One Calculator &amp; Converter Hub</div>
        <div class="hero-subtitle">Choose a tool from the sidebar to get started.</div>
        """,
        unsafe_allow_html=True,
    )


def render_home() -> None:
    """Render the complete home page."""
    _render_top_header()
    _render_page_title()
    _render_hero()
