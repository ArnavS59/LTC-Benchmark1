import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from utils import *
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
# from widgets import *
from alerts import *



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
    
    if not st.session_state['authenticated']:
        handle_login()
    else:
        st.title('Risk Management Dashboard')   
        display_upload_button()
        # col1 = st.columns(1)
        # data=fetch_contracts()
        # df=process_contracts(data)
        # df2=df.copy()
        # with col1:
            # data=fetch_contracts()
            # df=process_contracts(data)

        col44, col45, col123=st.columns(3)
        with col44:
                # plot_revenue_graph()
                # display_expring(df)
                
            display_potential_liability()
                
        with col45:
            display_alert()
        
        with col123:
            display_opp()
                # display_contracts_renew(df)
                
                # st.metric("Contracts Signed this month", "12", border=True, delta="18")
                # plot_value_distribution()
                # plot_treemap()



            
            
        # with col2:
        #         st.header("Upload your contract file")
        #         # Create a file uploader in the second column
        #         uploaded_file = st.file_uploader("Choose a file")
                
                
                
        #         if uploaded_file:
        #             upload_contract(uploaded_file)
                    # upload_contract_google(uploaded_file)
                    
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

