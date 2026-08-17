import streamlit as st

from api.area_converter_api import convert_area


def render_area_converter():

    # ==========================================
    # Header
    # ==========================================

    st.markdown(
        """
        <div class="converter-hero">
            <div class="hero-icon">📐</div>
            <div>
                <h1>Area Converter</h1>
                <p>Convert between different area units instantly.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # ==========================================
    # Converter Card
    # ==========================================

    st.markdown(
        """
        <div class="converter-card">
            <h2>Convert Area</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ==========================================
    # Inputs
    # ==========================================

    col1, col2, col3 = st.columns([1.2, 1.1, 1.1])

    with col1:

        value = st.number_input(
            "Value",
            min_value=0.0,
            value=10000.0,
            step=1.0,
        )

    units = [
        "square_meter",
        "square_kilometer",
        "square_centimeter",
        "square_mile",
        "square_yard",
        "square_foot",
        "square_inch",
        "acre",
        "hectare",
    ]

    with col2:

        from_unit = st.selectbox(
            "From Unit",
            units,
        )

    with col3:

        to_unit = st.selectbox(
            "To Unit",
            units,
        )

    # ==========================================
    # Convert Button
    # ==========================================

    st.markdown(
        "<div style='text-align:center;'>",
        unsafe_allow_html=True,
    )

    convert_button = st.button(
        "⇄  Convert",
        use_container_width=False,
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    # ==========================================
    # API Call
    # ==========================================

    if convert_button:

        response = convert_area(
            value=value,
            from_unit=from_unit,
            to_unit=to_unit,
        )

        if "error" in response:

            st.error(response["error"])

        else:

            result = response["result"]

            # ==================================
            # Result Card
            # ==================================

            st.markdown(
                f"""
                <div class="result-card">

                    <div class="result-icon">
                        ✓
                    </div>

                    <div class="result-content">

                        <p class="result-label">
                            Result
                        </p>

                        <h2>
                            {result}
                        </h2>

                        <h3>
                            {to_unit}
                        </h3>

                        <p>
                            {value} {from_unit}
                            =
                            {result} {to_unit}
                        </p>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

    # ==========================================
    # Bottom Information
    # ==========================================

    st.markdown(
        """
        <div class="bottom-grid">

            <div class="info-card">

                <h2>Supported Area Units</h2>

                <div class="unit-list">

                    <span>square_meter</span>
                    <span>square_kilometer</span>
                    <span>square_centimeter</span>
                    <span>square_mile</span>
                    <span>square_yard</span>
                    <span>square_foot</span>
                    <span>square_inch</span>
                    <span>acre</span>
                    <span>hectare</span>

                </div>

            </div>

            <div class="info-card">

                <h2>💡 Did you know?</h2>

                <p>
                    1 hectare is equal to
                    10,000 square meters.
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )