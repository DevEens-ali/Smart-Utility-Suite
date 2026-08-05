import streamlit as st
from api.calculator_api import calculate_basic


def render_basic_calculator():

    # ==========================
    # Title
    # ==========================
    st.title("🧮 Basic Calculator")
    st.write("Perform simple arithmetic operations.")

    st.divider()

    # ==========================
    # Inputs
    # ==========================
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input(
            "First Number",
            value=0.0,
            step=1.0,
        )

    with col2:
        num2 = st.number_input(
            "Second Number",
            value=0.0,
            step=1.0,
        )

    operation = st.selectbox(
        "Operation",
        [
            "+",
            "-",
            "*",
            "/",
        ],
    )

    st.divider()

    # ==========================
    # Calculate Button
    # ==========================
    if st.button(
        "Calculate",
        use_container_width=True,
    ):

        response = calculate_basic(
            num1=num1,
            num2=num2,
            operation=operation,
        )

        # ==========================
        # Success
        # ==========================
        if "result" in response:

            st.success("Calculation completed successfully.")

            st.subheader("Result")

            st.metric(
                label="Answer",
                value=response["result"],
            )

            # Debug (remove later)
        

        # ==========================
        # Error
        # ==========================
        else:

            st.error(
                response.get(
                    "error",
                    "Something went wrong."
                )
            )