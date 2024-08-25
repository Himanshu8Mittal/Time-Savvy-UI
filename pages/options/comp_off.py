"""Comp-Off section of the Application"""

import streamlit as st
import requests
from datetime import datetime, date, timedelta


def show_comp_off(user_profile):
    st.title("Comp-Off")

    indxx_id = user_profile["indxx_id"]
    
    if user_profile["role"] is not None:
        col1, col2 = st.columns(2)
        with col1:
            if user_profile["role"]["is_admin"]:
                indxx_id = st.text_input("Indxx ID")
    
        

    days_in_month = (
        datetime(date.today().year, date.today().month % 12 + 1, 1) - timedelta(days=1)
    ).day

    col1, col2 = st.columns(2)

    with col1:
        from_date = st.date_input(
            "From Date",
            value=date.today(),
            min_value=date.today().replace(day=1),
            max_value=date.today().replace(day=days_in_month),
        )

        transaction_status = st.selectbox(
            "Status", options=["NOT AVAILED", "AVAILED"], index=0
        )

    with col2:
        to_date = st.date_input(
            "To Date",
            value=date.today(),
            min_value=date.today().replace(day=1),
            max_value=date.today().replace(day=days_in_month),
        )

    from_date_str = from_date.isoformat()
    to_date_str = to_date.isoformat()

    if st.button("Submit"):
        if indxx_id == '':
            st.error("Please enter Indxx ID")
        else:    
            if from_date_str <= to_date_str:
                rr = requests.post(
                    "http://127.0.0.1:8000/comp_off",
                    json={
                        "indxx_id": indxx_id,
                        "from_date": from_date_str,
                        "to_date": to_date_str,
                        "transaction_status": transaction_status,
                    },
                    timeout=10,
                )
                response = rr.json()

                if response["detail"] == "Comp Off data added successfully":
                    st.success("Comp Off data added successfully")
                else:
                    st.error(response["detail"])

            else:
                st.error("'From date' should be less than 'To date'")
