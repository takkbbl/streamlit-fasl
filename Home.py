import streamlit as st
import helpers as helpers
from streamlit_extras.switch_page_button import switch_page
from authentication import Authentication


def main():
    st.set_page_config(
        page_title="Symanto Active Few-Shot Learning",
        page_icon="https://developer.symanto.com/favicon.ico",
    )
    helpers.add_logo()

    auth = Authentication()

    st.title("Symanto's Active Learning Platform")
    st.write("Symanto Brain is an artificial intelligence model generation engine developed by Symanto, which helps you "
             "to create classification models for any use case and from multiple data sources with only a few or no "
             "provided examples at all. By using Symanto Brain, one reduces the time and economic cost of generating a "
             "model, and also eliminates the bias and streamlines the generation process. ")
    st.write("Symanto Brain allows a deep "
             "understanding of the meaning of the analysed text and its context. It works well in scenarios with denial "
             "and a certain level of irony and sarcasm, as well as in texts that contain references to the knowledge of "
             "the world (e.g., I would like Lady Gaga's job).")

    subscription_key = st.text_input("Please add your API key to get started", "", type="password")
    if not subscription_key:
        return

    if not auth.is_valid_subscription_key(subscription_key):
        st.error("Invalid subscription key")
        return

    st.success("Congrats, you're ready to get started")

    if st.button("Create your first model", type="primary"):
        switch_page("Create new")

    st.write("or...")

    if st.button("Browse existing models", type="secondary"):
        switch_page("Models")


if __name__ == "__main__":
    main()
