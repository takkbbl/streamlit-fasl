import streamlit as st
import helpers as helpers

st.set_page_config(
        page_title="Symanto Active Few-Shot Learning",
        page_icon="https://developer.symanto.com/favicon.ico",
    )

helpers.add_logo()

st.title("Datasets")

tab1, tab2, tab3 = st.tabs(["All Datasets", "Add new", "Delete"])

with tab1:
    obj = {
        "0": "Dataset 1",
        "1": "Dataset 2",
        "2": "Dataset 3"
    }
    st.json(obj)

with tab2:
    st.file_uploader("Upload your dataset")

with tab3:
    selected_dataset = st.selectbox(
        'Select your dataset',
        ('Dataset 1', 'Dataset 2', 'Dataset 3'))
    st.error(f"This action is irreversible. Do you really want to delete {selected_dataset}?")

    deleted = st.button(f"Delete {selected_dataset}")
    if deleted:
        st.write("Dataset deleted")

