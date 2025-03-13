
import streamlit as st

# Import the pages
from unit_circle import main as unit_circle_main
from trigonometric_functions import main as trigonometric_functions_main

st.set_page_config(page_title="QuCreate Streamlit Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Multi-page setup
page = st.sidebar.selectbox("Select a page:", ["Unit Circle Explorer", "Trigonometric Functions"])

if page == "Unit Circle Explorer":
    unit_circle_main()
elif page == "Trigonometric Functions":
    trigonometric_functions_main()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
