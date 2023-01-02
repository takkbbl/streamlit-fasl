import streamlit as st
import helpers as helpers
from streamlit_extras.switch_page_button import switch_page

helpers.add_logo()

st.title("Symanto's Active Learning Platform")
st.write("Symanto Brain is an artificial intelligence model generation engine developed by Symanto, which helps you "
         "to create classification models for any use case and from multiple data sources with only a few or no "
         "provided examples at all. By using Symanto Brain, one reduces the time and economic cost of generating a "
         "model, and also eliminates the bias and streamlines the generation process. ")
st.write("Symanto Brain allows a deep "
         "understanding of the meaning of the analysed text and its context. It works well in scenarios with denial "
         "and a certain level of irony and sarcasm, as well as in texts that contain references to the knowledge of "
         "the world (e.g., I would like Lady Gaga's job).")


if st.button("Create your first model", type="primary"):
    switch_page("Create new")

st.write("or...")

if st.button("Browse existing models", type="secondary"):
    switch_page("Models")

