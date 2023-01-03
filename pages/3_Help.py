import streamlit as st
import helpers as helpers

st.set_page_config(
        page_title="Symanto Active Few-Shot Learning",
        page_icon="https://developer.symanto.com/favicon.ico",
    )

helpers.add_logo()

st.title("Help")
st.markdown("If you need any help, please visit our knowlege base [Symanto Brain Knowledge Base]("
            "https://symanto.atlassian.net/wiki/spaces/SYM/overview).")
st.markdown("For questions, feedback or improvement suggestions, you can reach us also via"
            " [support@symanto.com](mailto:support@symanto.com).")