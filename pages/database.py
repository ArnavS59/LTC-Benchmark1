import streamlit as st
from utils import *
from extraction import process_contracts


# Check if the user is authenticated
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def db_page():
    COL1, COL2 = st.columns([3,1])
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
    else:
        with COL1:
            st.title("Overview of all Contracts")
            data=fetch_contracts()
            df=process_contracts(data)
            st.dataframe(df)
        with COL2:
            st.header("Upload your contract file")
                # Create a file uploader in the second column
            uploaded_file = st.file_uploader("Choose a file")
                
                
                
            if uploaded_file:
                upload_contract(uploaded_file)

if __name__ == "__main__":
        db_page()