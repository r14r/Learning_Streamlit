import streamlit as st


def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

pages = {
    "Your account": [
        st.Page("pages/create_account.py", title="Create your account"),
        st.Page("pages/manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("pages/learn.py", title="Learn about us"),
        st.Page("pages/trial.py", title="Try it out"),
    ],
    "Widgets": [
        page1,
        page2,
    ],
}



# -------------------------------------------------------------------------------------------------
if "top" not in st.session_state:
    st.session_state.top = False

top = "top" if st.session_state.top else "sidebar"


# -------------------------------------------------------------------------------------------------
st.sidebar.checkbox("Top Navigation", key="top")

st.sidebar.selectbox("Foo", ["A", "B", "C"], key="foo")
st.sidebar.checkbox("Bar", key="bar")

# -------------------------------------------------------------------------------------------------
pg = st.navigation(pages, position=top)

pg.run()