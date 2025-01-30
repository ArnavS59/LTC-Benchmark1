import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
from alerts import cardliab, cardopp, cardalert

from utils import *

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def main():
    
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
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

        # col44, col45, col123=st.columns(3)
        # with col44:

        #     # display_potential_liability()
        #     cardliab()
                
        # with col45:
        #     cardalert()
            # display_alert()
        
        # with col123:
            # display_opp()
        cardopp()
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