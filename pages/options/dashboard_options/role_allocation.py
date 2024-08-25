import streamlit as st
from utility.data import employee_data
import requests


def role_allocation():
    st.markdown(
        """
    <style>
        .stRadio > div {
            display: flex;
            flex-direction: row;
        }
        .stRadio > div > label {
            margin-right: 10px;
        }
    </style>
        """,
        unsafe_allow_html=True,
    )
    indxx_id = st.text_input("Enter Indxx ID")
    role = st.radio("Select a role", ("Super User", "Admin", "User"))
    if st.button("Submit Role"):
        if indxx_id:
            resp = employee_data(indxx_id)
            if resp["indxx_id"] == indxx_id:
                data = {"indxx_id": indxx_id, "role": role}
                if data["role"] == "Super User":
                    data["is_super_user"] = "true"
                    data["is_admin"] = "true"
                elif data["role"] == "Admin":
                    data["is_super_user"] = "false"
                    data["is_admin"] = "true"
                else:
                    data["is_super_user"] = "false"
                    data["is_admin"] = "false"
                del data["role"]
                rr = requests.post(
                    "http://127.0.0.1:8000/create_role/", json=data, timeout=10
                )
                response = rr.json()

                if rr.status_code == 200:
                    st.text(response["message"])

            else:
                st.error("Please enter a valid Indxx ID")
        else:
            st.error("Please enter an Indxx ID")
