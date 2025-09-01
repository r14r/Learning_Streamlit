import os

import streamlit as st

HERE=os.path.dirname(os.path.dirname(__file__))

HORIZONTAL_RED = "assets/img/horizontal_red.png"
ICON_RED = "assets/img/icon_red.png"
HORIZONTAL_BLUE = "assets/img/horizontal_blue.png"
ICON_BLUE = "assets/img/icon_blue.png"

options = [HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)
main_body_logo = st.selectbox("Main body logo", options, 1)

st.write(f"Logo: {sidebar_logo}")

st.logo(
    f"{HERE}/{sidebar_logo}",
    icon_image=f"{HERE}/{main_body_logo}",
)
st.sidebar.markdown("Hi!")
