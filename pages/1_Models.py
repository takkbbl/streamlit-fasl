import streamlit as st
import helpers as helpers

st.set_page_config(
        page_title="Symanto Active Few-Shot Learning",
        page_icon="https://developer.symanto.com/favicon.ico",
    )

helpers.add_logo()

st.title("Models")

selected_model = st.selectbox(
    'Select your model from the list',
    ('Model 1', 'Model 2', 'Model 3'))

#else:
    #st.header("Wizard to create a new model")
    #st.button("Go back")
    #if go_back:
    #

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Describe", "Inspect", "Update",
                                                    "Run", "Evaluate", "Download", "Delete"])

with tab1:
    st.markdown(f"**Model:** {selected_model}  \n  \n"
                "**Status:** Ready  \n  \n"
                "**Language:** en  \n  \n"
                "**Description:** A few-shot sentiment analysis model.")

with tab2:
    st.write("Not enough data for plotting model quality. Add more iterations.")

with tab3:
    # st.subheader("Update")
    mode = st.selectbox("Please choose a mode: ", ("Requests", "File Upload"))
    if mode == "Requests":
        sampler = st.selectbox("Please select a sampler method: ", ("Random", "Margin"))
        n_instances = st.slider('n_instances', 4, 64)
        request = st.button("Request")
    else:
        st.file_uploader("Choose a file")

with tab4:
    deployment_type = st.selectbox("Please select a deployment type", ("Demo", "File", "FASL REST"))
    if deployment_type == "Demo":
        st.text_input("Insert a sample text", value="This text will be classified by the model")
    elif deployment_type == "File":
        run_file = st.file_uploader("Choose a file", key="unique")
    else:
        st.markdown("**Please note:** Replace *FASL_API_KEY* with your subscription key.")
        st.code("curl -X 'POST'   \n    'https://api.symanto.net/active-learning/v2/26/predict'   \n    -H 'accept: application/json' "
                "  \n    -H 'Content-Type: application/json'   \n    -H  'x-caller-id: ${FASL_API_KEY}' \   \n ...", language="xmlDoc")
with tab5:
    st.file_uploader("Upload a file")

with tab6:
    st.selectbox("What do you want to download?", ("Labelled examples", "Unlabelled examples"))
    st.selectbox("Format", ("csv", "tsv", "xlsx"))
    st.button("Download")

with tab7:
    st.error(f"This action is irreversible. Do you really want to delete this model?")

    deleted = st.button("Delete model")
    if deleted:
        st.write("Model deleted")
