import streamlit as st
from utils import *
from extraction import process_contracts
import pandas as pd

# Check if the user is authenticated
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def db_page():
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
    else:
        display_upload_button()
        COL1 = st.container()  
        with COL1:
            st.title("Overview of all Contracts")
        
        COL2, COL3, COL4, COL5 = st.columns([2,2,2,1])
        
        data=fetch_contracts()
        df=process_contracts(data)
        df['date_expiry'] = pd.to_datetime(df['date_expiry'])
        with COL2:
            selected_department = st.selectbox(
                "Select Department",
                ['Procurement', 'Sales', 'People'],
                key="department_select"
            )
        with COL3:
            if selected_department == "People":
                selected_contract_type = st.selectbox(
                    "Select Contract Type",
                    ['Employment Contract'],
                    key="contract_type_select"
                )
            
            elif selected_department == "Sales" :
                selected_contract_type=st.selectbox(
                "Select Contract Type",
                ['Investment Agreement'],
                key="contract_type_select"
            )
            elif selected_department=="Procurement":
                selected_contract_type=st.selectbox(
                "Select Contract Type",
                ['Purchase Agreement'],
                key="contract_type_select"
                )
        

        with COL4:
            
            min_value = int(df['contract_value'].min())
            max_value = int(df['contract_value'].max())

            # Slider to select the range
            contract_range = st.slider(
                "Select Contract Value Range",
                min_value=min_value,
                max_value=max_value,
                value=(min_value, max_value)
            )
            # filtered_df = filtered_df[
            #     (filtered_df['contract_value'] >= contract_range[0]) &
            #     (filtered_df['contract_value'] <= contract_range[1])
            # ]
        
        with COL5:
            options = ["Sent Out", "Reviewed", "Draft", "Signed", "Expired"]
            selection = st.pills("Status", options, selection_mode="single")
            current_date = pd.to_datetime("today")  # Get today's date
            # if selection == "Active":
            #     filtered_df = filtered_df[filtered_df['date_expiry'] >= current_date]
            # elif selection == "Expired":
            #     filtered_df = filtered_df[filtered_df['date_expiry'] < current_date]
            
        
        COL6 = st.container()  
        with COL6:
            filtered_df = df[
                (df['contract_value'] >= contract_range[0]) &
                (df['contract_value'] <= contract_range[1])
            ]

            if selected_department:
                filtered_df = filtered_df[filtered_df['department'] == selected_department]

            if selected_contract_type:
                filtered_df = filtered_df[filtered_df['contract_type'] == selected_contract_type]

            if selection == "Reviewed":
                filtered_df = filtered_df[filtered_df['status'] == "reviewed"]
            elif selection == "Sent Out":
                    filtered_df = filtered_df[filtered_df['status'] == "sent out"]
            elif selection == "Draft":
                    filtered_df = filtered_df[filtered_df['status'] == "draft"]
            elif selection == "Signed":
                    filtered_df = filtered_df[filtered_df['status'] == "signed"]
            elif selection == "Expired":
                filtered_df = filtered_df[filtered_df['date_expiry'] < current_date]
            
            st.dataframe(filtered_df)
                        


if __name__ == "__main__":
        db_page()