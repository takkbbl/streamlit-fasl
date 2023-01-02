import streamlit as st


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://symanto.atlassian.net/wiki/download/attachments/32773/atl.site.logo?version=1&modificationDate=1640006814606&cacheVersion=1&api=v2);
                background-repeat: no-repeat;
                background-size: 120px;
                padding-top: 0px;
                background-position: 20px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )