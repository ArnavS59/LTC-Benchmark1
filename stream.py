import streamlit as st
from extraction import *
import os
from dotenv import load_dotenv
load_dotenv()
from llm import call_llm
from utils import *
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False  # Initialize authentication status
        
if st.session_state['authenticated']:
            st.set_page_config(page_title="LTC Venture Dashboard", layout="wide", initial_sidebar_state="collapsed")  # Collapse the sidebar initially)
else:
        st.set_page_config(page_title="LTC Venture Dashboard", layout="centered",     initial_sidebar_state="collapsed")  # Collapse the sidebar initially

# Function to check credentials
def check_credentials(username, password):
    return username == USERNAME and password == PASSWORD
            
            
def handle_login():
    with st.form(key='login_form'):
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")
        
        if login_button:
            if check_credentials(username, password):
                st.session_state['authenticated'] = True
                st.success("Login successful!")
                st.rerun()  
            else:
                st.error("Invalid username or password.")


    
def main():
    st.title('LTC Venture Dashboard')
    
    if not st.session_state['authenticated']:
        handle_login()
    else:
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            data=fetch_contracts()
            st.write(data)
            # df=process_contracts(data)
            # st.write(df)
            # st.dataframe(df)
            
        with col2:
                st.header("Upload your contract file")
                # Create a file uploader in the second column
                uploaded_file = st.file_uploader("Choose a file")
                
                
                
                # if uploaded_file:
                            # Extract text from the uploaded file
                            # contract_text = extract_text_from_file(uploaded_file)
                            
                            # if contract_text:
                            #     with col1:
                            #         output=call_llm(contract_text)
                            #         st.write(output.rent, output.deposit)
                            
                            # with col1:
                            #     data=fetch_contracts()
                            #     df=process_contracts(data)
                            #     st.dataframe(df)
                                    
                            # else:
                                # st.error("Unsupported file type or error reading the file.")

        
        
if __name__ == "__main__":
    main()

