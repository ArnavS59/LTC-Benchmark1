import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px




def plot_revenue_graph(df):
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