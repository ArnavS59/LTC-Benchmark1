import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from utils import *
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
import pandas as pd
import plotly.express as px



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


    



def plot_revenue_graph():
    data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [200, 300, 400, 350, 500, 600],
    "Profit": [50, 80, 100, 90, 150, 200]
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Create Plotly line graph
    fig = px.line(
        df, 
        x="Month", 
        y=["Sales", "Profit"], 
        title="Monthly Sales and Profit Trends",
        labels={"value": "Amount ($)", "variable": "Metric"},
        markers=True
    )

    # Display the line graph in Streamlit
    st.plotly_chart(fig)
    
    
def plot_pie_chart():
    df=pd.DataFrame({
        "Contract Category": ["IT Services", "Consulting", "Construction", "IT Services", "Consulting", "Marketing"],
        "Item/Service": ["Software", "Advisory", "Building", "Hardware", "Strategy", "Ads"],
        "Contract Value": [20000, 15000, 50000, 30000, 20000, 10000],
        "Contract Volume": [5, 3, 8, 6, 2, 4]
    })
    fig = px.pie(
        df,
        names="Contract Category",
        values="Contract Volume",
        title="Contract Volume by Category",
        hole=0.3
    )
    st.plotly_chart(fig)

# Top Purchases by Value (Treemap)
def plot_treemap():
    df=pd.DataFrame({
        "Contract Category": ["IT Services", "Consulting", "Construction", "IT Services", "Consulting", "Marketing"],
        "Item/Service": ["Software", "Advisory", "Building", "Hardware", "Strategy", "Ads"],
        "Contract Value": [20000, 15000, 50000, 30000, 20000, 10000],
        "Contract Volume": [5, 3, 8, 6, 2, 4]
    })
    fig = px.treemap(
        df,
        path=["Contract Category", "Item/Service"],
        values="Contract Value",
        title="Top Purchases by Value",
    )
    st.plotly_chart(fig)

# Contract Value Distribution (Histogram)
def plot_value_distribution():
    df=pd.DataFrame({
        "Contract Category": ["IT Services", "Consulting", "Construction", "IT Services", "Consulting", "Marketing"],
        "Item/Service": ["Software", "Advisory", "Building", "Hardware", "Strategy", "Ads"],
        "Contract Value": [20000, 15000, 50000, 30000, 20000, 10000],
        "Contract Volume": [5, 3, 8, 6, 2, 4]
    })
    
    fig = px.histogram(
        df,
        x="Contract Value",
        nbins=10,
        title="Contract Value Distribution",
        labels={"x": "Contract Value", "y": "Count"},
    )
    st.plotly_chart(fig)
    

def main():
    if not st.session_state['authenticated']:
            handle_login()
    else:
        display_upload_button()
        
        col1, col2=st.columns([6,1])
        with col1:
            st.title('LTC Accountability Dashboard')
        with col2:
            displayexport()

        col44, col45, col11=st.columns(3)
        with col44:
                st.metric("Total Revenue", "€600k", border=True)

                
        with col45:
                st.metric("Contracts Signed this month", "12", border=True, delta="18")
                # test()
        with col11:
                st.metric("Average Contract Signing Duration", "15 days", border=True)

        
        COL123, COL12321 = st.columns(2)
        with COL123:
                plot_revenue_graph()
                plot_pie_chart()
        with COL12321:
                plot_value_distribution()
                plot_treemap()

main()