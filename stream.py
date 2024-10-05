import streamlit as st
from ml import *
import os

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

# Function to check credentials
def check_credentials(username, password):
    return username == USERNAME and password == PASSWORD

def display(col1, clauses):
    with col1:
        st.header("Contract Clauses")
        for idx, (clause, clause_type) in enumerate(clauses):
            st.write(f"**Clause {idx + 1}:**")
            st.write(clause)
            st.write(f"**Type:** {clause_type}")
            st.write("---")
            
            
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
                return True
            else:
                st.error("Invalid username or password.")
    return False  # Unsuccessful login

    
def main():
    st.set_page_config(layout="wide")
    st.title('LTC Venture Dashboard')
    
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False  # Initialize authentication status
        
    if not st.session_state['authenticated']:
        if handle_login():
            st.rerun()  
    else:
        col1, col2 = st.columns([3, 1])
                    
        with col2:
                st.header("Upload your contract file")
                # Create a file uploader in the second column
                uploaded_file = st.file_uploader("Choose a file")
                
                if uploaded_file:
                            # Extract text from the uploaded file
                            contract_text = extract_text_from_file(uploaded_file)
                            
                            if contract_text:
                                # Run clause identification on the contract text
                                clauses = identify_clauses(contract_text)
                                
                                # Display the extracted clauses in col1
                                display(col1, clauses)
                            else:
                                st.error("Unsupported file type or error reading the file.")

        
        
if __name__ == "__main__":
    main()

