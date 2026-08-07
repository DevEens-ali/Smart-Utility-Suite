import streamlit as st
from api.Bmi_api import calculate_bmi


def render_bmi_calculator():

    # ==========================
    # Page Header
    # ==========================

    st.title("⚖️ BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI).")

    st.divider()

    # ==========================
    # User Inputs
    # ==========================

    col1, col2 = st.columns(2)

    with col1:
        height = st.number_input(
            "Height (meters)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
        )

    with col2:
        weight = st.number_input(
            "Weight (kg)",
            min_value=0.0,
            step=0.1,
            format="%.1f",
        )

    st.divider()

    # ==========================
    # Calculate Button
    # ==========================

    if st.button(
        "Calculate BMI",
        use_container_width=True,
    ):

        response = calculate_bmi(
            height=height,
            weight=weight,
        )

        # ==========================
        # Error Response
        # ==========================

        if "error" in response:
            st.error(response["error"])

        # ==========================
        # Success Response
        # ==========================

        else:

            st.success("BMI calculated successfully.")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="BMI",
                    value=response["bmi"],
                )

            with col2:
                st.metric(
                    label="Category",
                    value=response["category"],
                )

            st.info(response["message"])

            st.subheader("💡 Health Advice")
            st.write(response["advice"])