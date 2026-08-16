import streamlit as st

from api.scientific_api import calculate_scientific


def render_scientific_calculator():

    # =========================================================
    # PAGE HEADER
    # =========================================================

    st.title("🔬 Scientific Calculator")
    st.write("Perform basic and advanced mathematical calculations.")

    st.divider()

    # =========================================================
    # SESSION STATE
    # =========================================================

    if "scientific_expression" not in st.session_state:
        st.session_state.scientific_expression = ""

    if "scientific_result" not in st.session_state:
        st.session_state.scientific_result = None

    # =========================================================
    # HELPER FUNCTIONS
    # =========================================================

    def add_to_expression(value):
        st.session_state.scientific_expression += value

    def clear_expression():
        st.session_state.scientific_expression = ""
        st.session_state.scientific_result = None

    def delete_last():
        st.session_state.scientific_expression = (
            st.session_state.scientific_expression[:-1]
        )

    # =========================================================
    # DISPLAY
    # =========================================================

    st.text_input(
        "Expression",
        key="scientific_expression",
        placeholder="Type using keyboard or use the buttons below...",
    )

    # =========================================================
    # SCIENTIFIC BUTTONS
    # =========================================================

    st.subheader("Scientific Functions")

    row1 = st.columns(5)

    with row1[0]:
        st.button(
            "√",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.sqrt(",),
        )

    with row1[1]:
        st.button(
            "sin",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.sin(",),
        )

    with row1[2]:
        st.button(
            "cos",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.cos(",),
        )

    with row1[3]:
        st.button(
            "tan",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.tan(",),
        )

    with row1[4]:
        st.button(
            "log",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.log10(",),
        )

    row2 = st.columns(5)

    with row2[0]:
        st.button(
            "ln",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.log(",),
        )

    with row2[1]:
        st.button(
            "π",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.pi",),
        )

    with row2[2]:
        st.button(
            "e",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.e",),
        )

    with row2[3]:
        st.button(
            "x²",
            use_container_width=True,
            on_click=add_to_expression,
            args=("**2",),
        )

    with row2[4]:
        st.button(
            "xʸ",
            use_container_width=True,
            on_click=add_to_expression,
            args=("**",),
        )

    row3 = st.columns(5)

    with row3[0]:
        st.button(
            "x!",
            use_container_width=True,
            on_click=add_to_expression,
            args=("math.factorial(",),
        )

    with row3[1]:
        st.button(
            "1/x",
            use_container_width=True,
            on_click=add_to_expression,
            args=("1/(",),
        )

    with row3[2]:
        st.button(
            "(",
            use_container_width=True,
            on_click=add_to_expression,
            args=("(",),
        )

    with row3[3]:
        st.button(
            ")",
            use_container_width=True,
            on_click=add_to_expression,
            args=(")",),
        )

    with row3[4]:
        st.button(
            "%",
            use_container_width=True,
            on_click=add_to_expression,
            args=("%",),
        )

    st.divider()

    # =========================================================
    # NUMERIC KEYPAD
    # =========================================================

    st.subheader("Calculator")

    # ---------------------------------------------------------
    # 7 8 9 ÷
    # ---------------------------------------------------------

    row = st.columns(4)

    with row[0]:
        st.button(
            "7",
            use_container_width=True,
            on_click=add_to_expression,
            args=("7",),
        )

    with row[1]:
        st.button(
            "8",
            use_container_width=True,
            on_click=add_to_expression,
            args=("8",),
        )

    with row[2]:
        st.button(
            "9",
            use_container_width=True,
            on_click=add_to_expression,
            args=("9",),
        )

    with row[3]:
        st.button(
            "÷",
            use_container_width=True,
            on_click=add_to_expression,
            args=("/",),
        )

    # ---------------------------------------------------------
    # 4 5 6 ×
    # ---------------------------------------------------------

    row = st.columns(4)

    with row[0]:
        st.button(
            "4",
            use_container_width=True,
            on_click=add_to_expression,
            args=("4",),
        )

    with row[1]:
        st.button(
            "5",
            use_container_width=True,
            on_click=add_to_expression,
            args=("5",),
        )

    with row[2]:
        st.button(
            "6",
            use_container_width=True,
            on_click=add_to_expression,
            args=("6",),
        )

    with row[3]:
        st.button(
            "×",
            use_container_width=True,
            on_click=add_to_expression,
            args=("*",),
        )

    # ---------------------------------------------------------
    # 1 2 3 -
    # ---------------------------------------------------------

    row = st.columns(4)

    with row[0]:
        st.button(
            "1",
            use_container_width=True,
            on_click=add_to_expression,
            args=("1",),
        )

    with row[1]:
        st.button(
            "2",
            use_container_width=True,
            on_click=add_to_expression,
            args=("2",),
        )

    with row[2]:
        st.button(
            "3",
            use_container_width=True,
            on_click=add_to_expression,
            args=("3",),
        )

    with row[3]:
        st.button(
            "−",
            use_container_width=True,
            on_click=add_to_expression,
            args=("-",),
        )

    # ---------------------------------------------------------
    # 0 . 00 +
    # ---------------------------------------------------------

    row = st.columns(4)

    with row[0]:
        st.button(
            "0",
            use_container_width=True,
            on_click=add_to_expression,
            args=("0",),
        )

    with row[1]:
        st.button(
            ".",
            use_container_width=True,
            on_click=add_to_expression,
            args=(".",),
        )

    with row[2]:
        st.button(
            "00",
            use_container_width=True,
            on_click=add_to_expression,
            args=("00",),
        )

    with row[3]:
        st.button(
            "+",
            use_container_width=True,
            on_click=add_to_expression,
            args=("+",),
        )

    st.divider()

    # =========================================================
    # CONTROL BUTTONS
    # =========================================================

    row = st.columns(3)

    with row[0]:

        st.button(
            "🗑️ Clear",
            use_container_width=True,
            on_click=clear_expression,
        )

    with row[1]:

        st.button(
            "⌫ Backspace",
            use_container_width=True,
            on_click=delete_last,
        )

    with row[2]:

        calculate_pressed = st.button(
            "＝ Calculate",
            use_container_width=True,
        )

    # =========================================================
    # CALCULATE
    # =========================================================

    if calculate_pressed:

        expression = st.session_state.scientific_expression.strip()

        if not expression:

            st.warning("Please enter an expression.")

        else:

            response = calculate_scientific(expression)

            if "error" in response:

                st.error(response["error"])

            else:

                st.session_state.scientific_result = response["result"]

    # =========================================================
    # RESULT
    # =========================================================

    if st.session_state.scientific_result is not None:

        st.divider()

        st.subheader("📊 Result")

        col1, col2 = st.columns(2)

        with col1:

            st.write("Expression")

            st.code(
                st.session_state.scientific_expression,
                language="text",
            )

        with col2:

            st.write("Result")

            st.success(
                str(st.session_state.scientific_result)
            )
