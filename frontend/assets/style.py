"""
Central place for all custom CSS.

Streamlit alone cannot express exact borders/spacing/hover states the way
the reference design needs, so we inject scoped CSS via st.markdown.
No JS, no external frontend frameworks (React/Bootstrap-CSS/Tailwind) are
used - this is plain CSS styling native Streamlit elements.

The icon font (Bootstrap Icons) is bundled locally under assets/fonts and
loaded as a base64 data URI, so the app works fully offline and doesn't
depend on any external CDN being reachable.
"""

import base64
import os

import streamlit as st
from config.settings import COLORS

_FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts", "bootstrap-icons.woff2")


@st.cache_resource
def _load_icon_font_base64() -> str:
    """Read the local icon font once and cache it as a base64 string."""
    with open(_FONT_PATH, "rb") as font_file:
        return base64.b64encode(font_file.read()).decode("utf-8")


def apply_custom_css() -> None:
    """Inject global CSS. Call once, near the top of app.py."""
    icon_font_b64 = _load_icon_font_base64()

    st.markdown(
        f"""
        <style>
            /* Bootstrap Icons font, loaded locally (no external CDN needed) */
            @font-face {{
                font-family: "bootstrap-icons";
                src: url(data:font/woff2;base64,{icon_font_b64}) format("woff2");
                font-weight: normal;
                font-style: normal;
            }}
            .bi::before {{
                font-family: "bootstrap-icons" !important;
                font-style: normal;
                font-weight: normal !important;
                display: inline-block;
                line-height: 1;
            }}
            /* Glyph codepoints for the specific icons used on this page */
            .bi-house-door::before {{ content: "\\f423"; }}
            .bi-calculator::before {{ content: "\\f1e0"; }}
            .bi-graph-up::before {{ content: "\\f3f2"; }}
            .bi-mortarboard::before {{ content: "\\f6fe"; }}
            .bi-book::before {{ content: "\\f194"; }}
            .bi-heart-pulse::before {{ content: "\\f76f"; }}
            .bi-person::before {{ content: "\\f4e1"; }}
            .bi-percent::before {{ content: "\\f4d1"; }}
            .bi-sun::before {{ content: "\\f5a2"; }}

            /* Hide default Streamlit chrome for a clean, app-like look */
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}

            /* Overall page background */
            .stApp {{
                background-color: {COLORS['content_bg']};
            }}

            /* Sidebar container */
           /* Sidebar container */
section[data-testid="stSidebar"] {{
    background-color: {COLORS['sidebar_bg']};
    border-right: 1px solid {COLORS['border_color']};
    width: 280px !important;
}}

            /* Make the sidebar scrollable when content grows */
            section[data-testid="stSidebar"] > div:first-child {{
                overflow-y: auto;
                max-height: 100vh;
            }}

            /* Remove default top padding so content sits like the reference */
            .block-container {{
                padding-top: 2rem;
                padding-bottom: 2rem;
            }}
            section[data-testid="stSidebar"] .block-container {{
                padding-top: 1.25rem;
            }}

            /* Sidebar section labels (e.g. CALCULATORS) */
            .sidebar-section-title {{
                color: #6B7280;
                font-size: 13px;
                font-weight: 700;
                text-transform: uppercase;
                margin: 18px 0 8px 2px;
            }}

            /* Brand / logo row at the top of the sidebar */
            .sidebar-brand {{
                    color: #2563EB;
                    font-size: 24px;
                    font-weight: bold;
                
            }}
            .sidebar-brand-icon {{
                background-color: {COLORS['primary_blue']};
                color: white;
                border-radius: 8px;
                width: 34px;
                height: 34px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.05rem;
            }}
            .sidebar-brand-text {{
                font-size: 1.25rem;
                font-weight: 700;
                color: {COLORS['primary_blue']};
            }}

            /* Top-right header bar (theme icon) */
            .top-header-row {{
                display: flex;
                justify-content: flex-end;
                padding: 0.2rem 0 0.2rem 0;
            }}

            /* Hero icon box in the center of the home page */
            .hero-icon-box {{
                width: 148px;
                height: 148px;
                margin: 2.5rem auto 1.6rem auto;
                border: 2.5px solid {COLORS['primary_blue']};
                border-radius: 22px;
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: {COLORS['content_bg']};
            }}
            .hero-icon-box i {{
                font-size: 4.2rem;
                color: {COLORS['primary_blue']};
            }}

            .hero-title {{
                text-align: center;
                font-size: 1.6rem;
                font-weight: 700;
                color: {COLORS['text_dark']};
                margin-bottom: 0.4rem;
            }}
            .hero-subtitle {{
                text-align: center;
                font-size: 0.95rem;
                color: {COLORS['text_gray']};
            }}

            .page-title {{
                font-size: 2rem;
                font-weight: 700;
                color: {COLORS['text_dark']};
                margin-bottom: 0.2rem;
            }}
            .page-title span {{
                color: {COLORS['primary_blue']};
            }}
            .page-subtitle {{
                font-size: 1rem;
                color: {COLORS['text_gray']};
                margin-bottom: 1.2rem;
            }}

            hr.custom-divider {{
                border: none;
                border-top: 1px solid {COLORS['border_color']};
                margin: 0.5rem 0 0 0;
            }}
            /* ==========================================================
SIDEBAR BUTTONS
========================================================== */

section[data-testid="stSidebar"] .stButton {{
    width: 100%;
}}

section[data-testid="stSidebar"] .stButton > button {{

    width: 100%;

    background: white;

    color: #111827;

    border: 1px solid #E5E7EB;

    border-radius: 10px;

    padding: 8px 14px;

    text-align: left;

    font-size: 15px;

    font-weight: 500;

    transition: all 0.2s ease;

    margin-bottom: 6px;

    box-shadow: none;
}}

/* Hover Effect */

section[data-testid="stSidebar"] .stButton > button:hover {{

    background: #EFF6FF;

    color: #2563EB;

    border-color: #2563EB;

}}

/* Button when clicked */

section[data-testid="stSidebar"] .stButton > button:focus {{

    border-color: #2563EB;

    box-shadow: none;

}}
/* ===========================
   Sidebar Headings
=========================== */

section[data-testid="stSidebar"] h1{{
    color:#2563EB !important;
    font-size:28px !important;
    font-weight:700 !important;
}}

section[data-testid="stSidebar"] h3{{
    color:#6B7280 !important;
    font-size:13px !important;
    font-weight:700 !important;
    text-transform:uppercase;
    margin-top:15px !important;
    margin-bottom:8px !important;
}}

















            </style>
        """,
        unsafe_allow_html=True,
    )
