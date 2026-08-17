import streamlit as st


def render_sidebar():

    with st.sidebar:

        # ==========================================
        # BRAND
        # ==========================================

        st.title("🧮 UtilityHub")
        st.caption("Smart Calculators & Converters")

        st.divider()

        # ==========================================
        # HOME
        # ==========================================

        if st.button(
            "Home",
            icon=":material/home:",
            use_container_width=True,
            key="sidebar_home",
        ):
            st.session_state.page = "Home"

        # ==========================================
        # CALCULATORS
        # ==========================================

        st.markdown("### CALCULATORS")

        calculators = [
            ("Basic Calculator", "calculate"),
            ("Scientific Calculator", "functions"),
            ("CGPA Calculator", "school"),
            ("GPA Calculator", "bar_chart"),
            ("BMI Calculator", "monitor_weight"),
            ("Age Calculator", "cake"),
            ("Percentage Calculator", "percent"),
        ]

        for label, icon in calculators:

            if st.button(
                label,
                icon=f":material/{icon}:",
                use_container_width=True,
                key=f"sidebar_{label}",
            ):
                st.session_state.page = label

        # ==========================================
        # CONVERTERS
        # ==========================================

        st.markdown("### CONVERTERS")

        converters = [
            ("Length Converter", "straighten"),
            ("Weight Converter", "fitness_center"),
            ("Temperature Converter", "device_thermostat"),
            ("Volume Converter", "water_drop"),
            ("Area Converter", "square_foot"),
        ]

        for label, icon in converters:

            if st.button(
                label,
                icon=f":material/{icon}:",
                use_container_width=True,
                key=f"sidebar_{label}",
            ):
                st.session_state.page = label

        # ==========================================
        # BOTTOM
        # ==========================================

        st.divider()

        if st.button(
            "About Us",
            icon=":material/info:",
            use_container_width=True,
            key="sidebar_about",
        ):
            st.session_state.page = "About Us"

        st.caption("UtilityHub • 2026")
