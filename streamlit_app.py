import streamlit as st

st.title("🎈 URL params demo")
screening_report_id = st.query_params.get("screening_report_id")
st.write(
    "Screening report ID: {}".format(screening_report_id)
)
