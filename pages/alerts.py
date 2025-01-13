import streamlit as st
from utils import *
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
from extraction import *

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def display_expring(df):
    df['date_expiry'] = pd.to_datetime(df['date_expiry'])
    
    # Get today's date and date one month from today
    today = datetime.now()
    next_month = today + timedelta(days=30)
    
    # Filter contracts expiring in the next month
    expiring_soon = df[(df['date_expiry'] >= today) & (df['date_expiry'] <= next_month)]
    print(expiring_soon)
    
    # Visualization with Plotly
    if not expiring_soon.empty:
        fig = px.scatter(
            expiring_soon,
            x='date_expiry',
            y='title',  # Assuming there's a 'contract_name' column for labels
            title=f"{len(expiring_soon)} Contracts Expiring in the Next Month",
        )
        fig.update_layout(xaxis_title='Expiry Date', yaxis_title='Contracts')
        st.plotly_chart(fig)
    else:
        st.info("No contracts are expiring in the next month.")





def help_page():
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
    else:
        st.title("Alerts")
        data=fetch_contracts()
        df=process_contracts(data)
        display_expring(df)        

if __name__ == "__main__":
        help_page()
