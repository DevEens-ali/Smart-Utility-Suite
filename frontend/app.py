import streamlit as st

# ==========================================
# CONFIG
# ==========================================

from config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)

# ==========================================
# STYLING
# ==========================================

from assets.style import apply_custom_css

# ==========================================
# SIDEBAR
# ==========================================

from components.sidebar import render_sidebar

# ==========================================
# HOME
# ==========================================

from components.home import render_home

# ==========================================
# CALCULATORS
# ==========================================

from components.calculators.basic_calculator import render_basic_calculator
from components.calculators.bmi_calculator import render_bmi_calculator
from components.calculators.age_calculator import render_age_calculator
from components.calculators.scientific_calculator import (
    render_scientific_calculator
)

# ==========================================
# CONVERTERS
# ==========================================

from components.calculators.area_converter import render_area_converter


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)


# ==========================================
# CUSTOM CSS
# ==========================================

apply_custom_css()


# ==========================================
# MAIN APPLICATION
# ==========================================

def main():

    # ------------------------------------------
    # Render Sidebar
    # ------------------------------------------

    selected_page = render_sidebar()


    # ------------------------------------------
    # Render Selected Page
    # ------------------------------------------

    if selected_page == "Basic Calculator":

        render_basic_calculator()

    elif selected_page == "Scientific Calculator":

        render_scientific_calculator()

    elif selected_page == "BMI Calculator":

        render_bmi_calculator()

    elif selected_page == "Age Calculator":

        render_age_calculator()

    elif selected_page == "Area Converter":

        render_area_converter()

    else:

        render_home()


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    main()
