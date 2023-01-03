import streamlit as st
import helpers as helpers
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
        page_title="Symanto Active Few-Shot Learning",
        page_icon="https://developer.symanto.com/favicon.ico",
    )

helpers.add_logo()

st.title("Create new model")
st.write("Build text analytics models with highest performance and lowest effort.")

selected_dataset = st.selectbox(
        'Select your dataset',
        ('Dataset 1', 'Dataset 2', 'Dataset 3'))
st.write("Don't have a dataset yet? Upload one here:")
if st.button("Manage datasets", type="secondary"):
    switch_page("Datasets")

language = st.selectbox(
        'Language',
        ('en', 'de'))

if st.button("Create"):
    switch_page("Models")

