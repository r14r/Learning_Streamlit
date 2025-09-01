import streamlit as st


def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

pages = {
    "Your account": [
        st.Page("src/navigation/pages/create_account.py", title="Create your account"),
        st.Page("src/navigation/pages/manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("src/navigation/pages/learn.py", title="Learn about us"),
        st.Page("src/navigation/pages/trial.py", title="Try it out"),
    ],
    "Widgets": [
        page1,
        page2,
    ],
}

# -------------------------------------------------------------------------------------------------
pg = st.navigation(pages, position='top')

pg.run()