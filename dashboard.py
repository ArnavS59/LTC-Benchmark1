import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from utils import *
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
import pandas as pd
import plotly.express as px
from extraction import process_contracts


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
        title="Top Purchase Categories by Contract Value",
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
    
from datetime import datetime, timedelta

def display_expring(df):
    df["date_expiry"] = pd.to_datetime(df["date_expiry"])

    # Get today's date and date one month from today
    today = datetime.now()
    next_month = today + timedelta(days=30)

    # Filter contracts expiring in the next month
    expiring_soon = df[(df["date_expiry"] >= today) & (df["date_expiry"] <= next_month)]
    expiring_soon["date_expiry_numeric"] = (
        pd.to_datetime(expiring_soon["date_expiry"]).astype(int) / 10**9
    )  # Convert to seconds

    # Visualization with Plotly
    if not expiring_soon.empty:
        fig = px.scatter(
            expiring_soon,
            x="date_expiry",
            y="title",  # Assuming there's a 'contract_name' column for labels
            title=f"{len(expiring_soon)} Contracts Expiring in the Next Month",
            color="date_expiry_numeric",
            color_continuous_scale="RdBu",  # Red for soon, blue for later,
            text=expiring_soon["date_expiry"].dt.strftime("%Y-%m-%d"),
        )
        fig.update_traces(
            marker=dict(size=12),  # Increase dot size
            textposition="bottom center",  # Position labels below dots
        )

        fig.update_layout(
            xaxis_title="Expiry Date", yaxis_title=None, coloraxis_showscale=False
        )
        st.plotly_chart(fig)
    else:
        st.info("No contracts are expiring in the next month.")


def display_contracts_renew(df):

    today = datetime.now()
    next_month = today + timedelta(days=30)
    # df['date_expiry'] = pd.to_datetime(df['date_expiry'])
    # expiring_soon = df[(df['date_expiry'] >= today) & (df['date_expiry'] <= next_month)]
    # today = datetime.now()
    # next_month = today + timedelta(days=30)

    # Filter contracts expiring in the next month
    expiring_soon = df[(df["date_expiry"] >= today) & (df["date_expiry"] <= next_month)]

    total_cost = expiring_soon["contract_value"].sum()

    expiring_soon["category"] = ""
    if not expiring_soon.empty:
        fig = px.bar(
            expiring_soon,
            x="category",  # Contract names
            y="contract_value",  # Cost to be paid for renewal
            color="contract_value",  # Color bars based on cost
            color_continuous_scale="Viridis",  # Color scale
            title=f"{len(expiring_soon)} Contracts Auto-Renewing in the Next Month with total cost of €{total_cost}",
            hover_data={
                "title": True,
                "contract_value": True,
            },  # Show contract title and cost on hover
        )

        # Customize chart layout
        fig.update_layout(
            barmode="stack",
            xaxis_title="Contracts",
            yaxis_title="Value (€)",
            coloraxis_colorbar_title="Cost",
        )

        # Display the chart
        st.plotly_chart(fig)

    else:
        st.write("No contracts expiring in the next month.")



def main():
    if not st.session_state['authenticated']:
            handle_login()
    else:
        display_upload_button()
        data=fetch_contracts()
        df=process_contracts(data)
        col1, col2=st.columns([6,1])
        with col1:
            st.title('Performance Metrics')
        with col2:
            displayexport()

        col44, col45, col11=st.columns(3)
        with col44:
                st.metric("Total Revenue", "€600k", border=True)

                
        with col45:
                st.metric("Contracts Signed this month", "12", border=True, delta="4")
                # test()
        with col11:
                st.metric("Average Contract Signing Duration", "15 days", border=True)

        
        COL123, COL12321 = st.columns(2)
        with COL123:
                plot_revenue_graph()
                plot_pie_chart()
                display_expring(df)
        with COL12321:
                plot_value_distribution()
                plot_treemap()
                display_contracts_renew(df)

main()