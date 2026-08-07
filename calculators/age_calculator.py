import streamlit as st
from datetime import date
from api.age_api import calculate_age


def render_age_calculator():

    # ======================================
    # Header
    # ======================================

    st.title("🎂 Age Calculator")
    st.write("Calculate your exact age with detailed insights.")

    st.divider()

    # ======================================
    # Date of Birth
    # ======================================

    date_of_birth = st.date_input(
        label="📅 Select Your Date of Birth",
        value=date(2000, 1, 1),          # Default Date
        min_value=date(1900, 1, 1),      # Earliest Date
        max_value=date.today(),          # Latest Date
        format="YYYY/MM/DD",
    )

    st.divider()

    # ======================================
    # Calculate Button
    # ======================================

    if st.button(
        "🎉 Calculate Age",
        use_container_width=True,
    ):

        response = calculate_age(str(date_of_birth))

        # ======================================
        # Error Handling
        # ======================================

        if "error" in response:
            st.error(response["error"])
            return

        # ======================================
        # Success
        # ======================================

        st.success("Age calculated successfully.")

        # ======================================
        # Current Age
        # ======================================

        st.subheader("🎂 Current Age")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Years", response["current_age"]["years"])

        with col2:
            st.metric("Months", response["current_age"]["months"])

        with col3:
            st.metric("Days", response["current_age"]["days"])

        st.divider()

        # ======================================
        # Lifetime Statistics
        # ======================================

        st.subheader("📊 Lifetime Statistics")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Months", response["total_age"]["months"])

        with col2:
            st.metric("Weeks", response["total_age"]["weeks"])

        with col3:
            st.metric("Days", response["total_age"]["days"])

        with col4:
            st.metric("Hours", response["total_age"]["hours"])

        with col5:
            st.metric("Minutes", response["total_age"]["minutes"])

        st.divider()

        # ======================================
        # Birth Details
        # ======================================

        st.subheader("🌟 Birth Details")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Day of Birth",
                response["birth_details"]["day_of_birth"],
            )

            st.metric(
                "Leap Year",
                "Yes ✅"
                if response["birth_details"]["born_in_leap_year"]
                else "No ❌",
            )

        with col2:
            st.metric(
                "Generation",
                response["birth_details"]["generation"],
            )

            st.metric(
                "Zodiac Sign",
                response["birth_details"]["zodiac_sign"],
            )

        st.divider()

        # ======================================
        # Next Birthday
        # ======================================

        st.subheader("🎉 Next Birthday")

        st.metric(
            "Days Remaining",
            response["next_birthday"]["days_remaining"],
        )

        st.divider()

        # ======================================
        # Fun Facts
        # ======================================

        st.subheader("💡 Fun Facts")

        st.info(
            f"""
❤️ You have lived **{response["total_age"]["days"]:,} days**

⏰ Approximately **{response["total_age"]["hours"]:,} hours**

🕒 Around **{response["total_age"]["minutes"]:,} minutes**
"""
        )
