import streamlit as st


def view():
    st.subheader('Home')

    with st.expander("ℹ️ User Guide", expanded=False):
        st.write("Home Page description goes here...")
