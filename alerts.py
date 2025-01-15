import streamlit as st
from utils import display_contracts
# from utils import *
# import pandas as pd
# from datetime import datetime, timedelta
# import plotly.express as px
from streamlit_pdf_viewer import pdf_viewer
# from extraction import *
from streamlit_card import card

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False


# def display_expring(df):
#     df["date_expiry"] = pd.to_datetime(df["date_expiry"])

#     # Get today's date and date one month from today
#     today = datetime.now()
#     next_month = today + timedelta(days=30)

#     # Filter contracts expiring in the next month
#     expiring_soon = df[(df["date_expiry"] >= today) & (df["date_expiry"] <= next_month)]
#     expiring_soon["date_expiry_numeric"] = (
#         pd.to_datetime(expiring_soon["date_expiry"]).astype(int) / 10**9
#     )  # Convert to seconds

#     # Visualization with Plotly
#     if not expiring_soon.empty:
#         fig = px.scatter(
#             expiring_soon,
#             x="date_expiry",
#             y="title",  # Assuming there's a 'contract_name' column for labels
#             title=f"{len(expiring_soon)} Contracts Expiring in the Next Month",
#             color="date_expiry_numeric",
#             color_continuous_scale="RdBu",  # Red for soon, blue for later,
#             text=expiring_soon["date_expiry"].dt.strftime("%Y-%m-%d"),
#         )
#         fig.update_traces(
#             marker=dict(size=12),  # Increase dot size
#             textposition="bottom center",  # Position labels below dots
#         )

#         fig.update_layout(
#             xaxis_title="Expiry Date", yaxis_title=None, coloraxis_showscale=False
#         )
#         st.plotly_chart(fig)
#     else:
#         st.info("No contracts are expiring in the next month.")


# def display_contracts_renew(df):

#     today = datetime.now()
#     next_month = today + timedelta(days=30)
#     # df['date_expiry'] = pd.to_datetime(df['date_expiry'])
#     # expiring_soon = df[(df['date_expiry'] >= today) & (df['date_expiry'] <= next_month)]
#     # today = datetime.now()
#     # next_month = today + timedelta(days=30)

#     # Filter contracts expiring in the next month
#     expiring_soon = df[(df["date_expiry"] >= today) & (df["date_expiry"] <= next_month)]

#     total_cost = expiring_soon["contract_value"].sum()

#     expiring_soon["category"] = ""
#     if not expiring_soon.empty:
#         fig = px.bar(
#             expiring_soon,
#             x="category",  # Contract names
#             y="contract_value",  # Cost to be paid for renewal
#             color="contract_value",  # Color bars based on cost
#             color_continuous_scale="Viridis",  # Color scale
#             title=f"{len(expiring_soon)} Contracts Auto-Renewing in the Next Month with total cost of €{total_cost}",
#             hover_data={
#                 "title": True,
#                 "contract_value": True,
#             },  # Show contract title and cost on hover
#         )

#         # Customize chart layout
#         fig.update_layout(
#             barmode="stack",
#             xaxis_title="Contracts",
#             yaxis_title="Value (€)",
#             coloraxis_colorbar_title="Cost",
#         )

#         # Display the chart
#         st.plotly_chart(fig)

#     else:
#         st.write("No contracts expiring in the next month.")


def display_potential_liability():
    styles = {
        "card": {
            "width": "100%",  # Make the card take the full width of its container
            "height": "auto",  # Height will adjust based on content
            # "background-color": "#f8f9fa",  # Light background color
            "border-radius": "10px",  # Rounded corners
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Subtle shadow for 3D effect
            "padding": "20px",  # Add some padding inside the card
            # "text-align": "left",
        },
        "title": {
            "background-color": "#FF9A3D",  # Light orange background
            "color": "white",  # White text color
            "padding": "10px",  # Padding around the title
            "border-radius": "5px",  # Slightly rounded corners for the title area
            "font-size": "24px",  # Adjust title font size
            "font-weight": "bold",  # Make the title bold
            "text-align": "left",
        },
        "text": {
            "font-size": "18px",  # Font size for the text
            "color": "#555",  # Gray color for the text
            "text-align": "left",  # Left-align the text
        },
        "line_break": {
            "margin-top": "10px",  # Space between text and the line break
            "margin-bottom": "10px",  # Space after line break
            "border-top": "1px solid #ddd",  # Add a separator line
        },
    }

    res = card(
        title="Potential Liability",
        text=["Cost Adaptive Clause", "Purchase_Agreement_Supplier02.pdf", '"The prices set forth in this agreement...."'],
        styles=styles,
    )
    return


def display_alert():
    styles = {
        "card": {
            "width": "100%",  # Make the card take the full width of its container
            "height": "auto",  # Height will adjust based on content
            # "background-color": "#f8f9fa",  # Light background color
            "border-radius": "10px",  # Rounded corners
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Subtle shadow for 3D effect
            "padding": "20px",  # Add some padding inside the card
            # "text-align": "left",
        },
        "title": {
            "background-color": "#FF9A3D",  # Light orange background
            "color": "white",  # White text color
            "padding": "10px",  # Padding around the title
            "border-radius": "5px",  # Slightly rounded corners for the title area
            "font-size": "24px",  # Adjust title font size
            "font-weight": "bold",  # Make the title bold
            "text-align": "left",
        },
        "text": {
            "font-size": "18px",  # Font size for the text
            "color": "#555",  # Gray color for the text
            "text-align": "left",  # Left-align the text
        },
        "line_break": {
            "margin-top": "10px",  # Space between text and the line break
            "margin-bottom": "10px",  # Space after line break
            "border-top": "1px solid #ddd",  # Add a separator line
        },
    }

    res1 = card(
        title="Alert",
        text=["Cost Adaptive Clause", "Renewing Contract in 10 Days $20,000", "SaaS Contract_Hubspot.pdf"],
        styles=styles,
        url="https://drive.google.com/file/d/1UBJiHDbc8nUQVzFlhPHYaH1mx1oAHUXO/view?usp=sharing"
    )
    return


# def help_page():
#     if not st.session_state['authenticated']:
#         st.warning("Please log in to access this page.")
#     else:
#         display_upload_button()
#         st.title("Alerts")
#         data=fetch_contracts()
#         df=process_contracts(data)
#         display_expring(df)
#         display_contracts_renew(df)

# if __name__ == "__main__":
#         help_page()
