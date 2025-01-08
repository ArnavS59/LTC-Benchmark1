import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

def display_expring(df):
    #given a df ewith colum daa_expiry use plotly to display expring contracts in the next month from todays date. See what visualization would wokr best. 
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
            # labels={'date_expiry': 'Expiry Date', 'title': 'Contract Name'},
            # text='contract_name'
        )
        fig.update_layout(xaxis_title='Expiry Date', yaxis_title='Contracts')
        st.plotly_chart(fig)
    else:
        st.info("No contracts are expiring in the next month.")

