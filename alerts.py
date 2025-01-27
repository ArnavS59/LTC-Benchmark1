# import streamlit as st
# from utils import display_contracts
# from utils import *
# import pandas as pd
# from datetime import datetime, timedelta
# import plotly.express as px
# from streamlit_pdf_viewer import pdf_viewer
# from extraction import *
from streamlit_card import card

# if "authenticated" not in st.session_state:
#     st.session_state["authenticated"] = False


def display_potential_liability():
    styles = {
        "card": {
            "width": "100%",  # Make the card take the full width of its container
            "height": "400px",  # Height will adjust based on content
            # "background-color": "#f8f9fa",  # Light background color
            "border-radius": "10px",  # Rounded corners
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Subtle shadow for 3D effect
            "padding": "10px 10px",  # Add some padding inside the card
            "text-align": "left", 
        },
        "title": {
            "background-color": "#FF9A3D",  # Light orange background
            "color": "white",  # White text color
            "padding": "10px",  # Padding around the title
            "border-radius": "5px",  # Slightly rounded corners for the title area
            "font-size": "24px",  # Adjust title font size
            "font-weight": "bold",  # Make the title bold
            "text-align": "top",
            "margin-bottom": "50px"
        },
        "text": {
            "font-size": "18px",  # Font size for the text
            "color": "#8a8787",  # Gray color for the text
            "text-align": "center",  # Left-align the text
            "margin": "10px 10px 10px 10px", #
        }
    }

    res = card(
        title="Potential Liability",
        text=["Cost Adaptive Clause", "Purchase_Agreement_BSH_02.pdf", '"The prices set forth in this agreement...."'],
        styles=styles,
    )
    return


def display_alert():
    styles = {
        "card": {
            "width": "100%",  # Make the card take the full width of its container
            "height": "400px",  # Height will adjust based on content
            # "background-color": "#f8f9fa",  # Light background color
            "border-radius": "10px",  # Rounded corners
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Subtle shadow for 3D effect
            "padding": "10px 10px",  # Add some padding inside the card
            "text-align": "left", 
        },
        "title": {
            "background-color": "#FF5733",  # Light orange background
            "color": "white",  # White text color
            "padding": "10px",  # Padding around the title
            "border-radius": "5px",  # Slightly rounded corners for the title area
            "font-size": "24px",  # Adjust title font size
            "font-weight": "bold",  # Make the title bold
            "text-align": "top",
            "margin-bottom": "50px"
        },
        "text": {
            "font-size": "18px",  # Font size for the text
            "color": "#8a8787",  # Gray color for the text
            "text-align": "center",  # Left-align the text
            "margin": "10px 10px 10px 10px", #
        }
    }

    res1 = card(
        title="Alert",
        text=["Renewing Contract in 10 Days with a Volume of  $20,000.", "SaaS_Contract_Hubspot.pdf" ,'"This Agreement shall automatically renew for successive year unless either party provides written notice of..."'],
        styles=styles,
        url="https://drive.google.com/file/d/1UBJiHDbc8nUQVzFlhPHYaH1mx1oAHUXO/view?usp=sharing"
    )
    return



def display_opp():
    styles = {
        "card": {
            "width": "100%",  # Make the card take the full width of its container
            "height": "400px",  # Height will adjust based on content
            # "background-color": "#f8f9fa",  # Light background color
            "border-radius": "10px",  # Rounded corners
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Subtle shadow for 3D effect
            "padding": "10px 10px",  # Add some padding inside the card
            "text-align": "left", 
        },
        "title": {
            "background-color": "green",  # Light orange background
            "color": "white",  # White text color
            "padding": "10px",  # Padding around the title
            "border-radius": "5px",  # Slightly rounded corners for the title area
            "font-size": "24px",  # Adjust title font size
            "font-weight": "bold",  # Make the title bold
            "text-align": "top",
            "margin-bottom": "50px"
        },
        "text": {
            "font-size": "18px",  # Font size for the text
            "color": "#8a8787",  # Gray color for the text
            "text-align": "center",  # Left-align the text
            "margin": "10px 10px 10px 10px", #
        }
    }


    res1 = card(
        title="Opportunity",
        text=["Mengenrabatt-Klausel","Purchase_Agreement_BSH_02.pdf",'"If the Purchaser buys 200 units of X in a single order, a discount of 50% on the total purchase value of the 500 units will apply."'],
        styles=styles,
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
import streamlit as st

# Define your HTML content

def cardliab():
    html_code = """
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alert Card</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: transparent;
            color: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-top: 100px;

        }
        .body:hover {
        transform: scale(1.05);
        }
        
        /* Base Card Styles (Dark Mode by default) */
        .card {
            width: 24rem;
            border: 1px solid #555;
            border-radius: 16px;
            background-color: #333;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
            padding: 1.5rem;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            height: 210px;

        }
        .card:hover {
        background-color:  #383838; /* Replace with your desired hover color */
         
}
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .card-header h2 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #f1f1f1;
            margin: 0;
        }
        .card-header .icon {
            color: #ff5722;
            margin-right: 0.5rem;
            font-size: 1.5rem;
        }
        .card-content {
            margin-bottom: 1rem;
        }
        .card-content p {
            font-size: 0.9rem;
            color: #bbb;
            margin: 0 0 0.5rem;
        }
        .file {
            background-color: #444;
            padding: 0.5rem;
            border-radius: 8px;
            color: #fff;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        blockquote {
            font-size: 0.9rem;
            color: #ddd;
            font-style: italic;
            border-left: 4px solid #555;
            padding-left: 0.5rem;
            margin: 0;
        }
        .card-footer {
            text-align: right;
        }
        .button {
            background-color: #007bff;
            color: #fff;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 0.9rem;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .button:hover {
            background-color: #0056b3;
            color: #fff;
        }
        .icon, .text {
        display: inline-block; /* Makes both elements align horizontally */
        margin-right: 10px; /* Adds space between them */
}

    </style>
</head>
<body>
    <div class="card">
        <div class="card-header">
       <h2 class="icon">⚠️</h2>
        <h2 class="text">Potential Liability</h2>

        </div>
        <div class="card-content">
            <p>Cost Adaptive Clause</p>
            <div class="file">Purchase_Agreement_BSH_02.pdf</div>
            <blockquote>"The prices set forth in this agreement are subject to adjustment based on changes in the cost of materials, labor, or other..."</blockquote>
        </div>
        <div class="card-footer">
            <a class="button">View Details</a>
        </div>
    </div>
</body>
</html>

    """

    # Use Streamlit to display the HTML
    return st.components.v1.html(html_code, height=500, scrolling=True)



def cardalert():
    html_code = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alert Card</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: transparent;
            color: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-top: 100px;

        }
        .body:hover {
        transform: scale(1.05);
        }
        
        /* Base Card Styles (Dark Mode by default) */
        .card {
            width: 24rem;
            border: 1px solid #555;
            border-radius: 16px;
            background-color: #333;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
            padding: 1.5rem;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            height: 210px;
        }
        .card:hover {
        background-color:  #383838; /* Replace with your desired hover color */
         
}
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .card-header h2 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #f1f1f1;
            margin: 0;
        }
        .card-header .icon {
            color: #ff5722;
            margin-right: 0.5rem;
            font-size: 1.5rem;
        }
        .card-content {
            margin-bottom: 1rem;
        }
        .card-content p {
            font-size: 0.9rem;
            color: #bbb;
            margin: 0 0 0.5rem;
        }
        .file {
            background-color: #444;
            padding: 0.5rem;
            border-radius: 8px;
            color: #fff;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        blockquote {
            font-size: 0.9rem;
            color: #ddd;
            font-style: italic;
            border-left: 4px solid #555;
            padding-left: 0.5rem;
            margin: 0;
        }
        .card-footer {
            text-align: right;
        }
        .button {
            background-color: #007bff;
            color: #fff;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 0.9rem;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .button:hover {
            background-color: #0056b3;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="card-header">
            <span class="icon">&#9888;</span>
            <h2>Alert</h2>
        </div>
        <div class="card-content">
            <p>Renewing Contract in 10 Days with a Volume of  $20,000.</p>
            <div class="file">SaaS_Contract_Hubspot.pdf</div>
            <blockquote>"This Agreement shall automatically renew for successive year unless either party provides written notice of..."</blockquote>
        </div>
        <div class="card-footer">
            <a href="https://drive.google.com/file/d/1UBJiHDbc8nUQVzFlhPHYaH1mx1oAHUXO/view?usp=sharing" target="_blank" class="button">View Details</a>
        </div>
    </div>
</body>
</html>
    """

    # Use Streamlit to display the HTML
    return st.components.v1.html(html_code, height=500, scrolling=True)




def cardopp():
    html_code = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alert Card</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: transparent;
            color: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-top: 100px;
        }
        .body:hover {
        transform: scale(1.05);
        }
        
        /* Base Card Styles (Dark Mode by default) */
        .card {
            width: 24rem;
            border: 1px solid #555;
            border-radius: 16px;
            background-color: #333;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
            padding: 1.5rem;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            height: 210px;
        }
        .card:hover {
        background-color:  #383838; /* Replace with your desired hover color */
         
}
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .card-header h2 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #f1f1f1;
            margin: 0;
        }
        .card-header .icon {
            color: #ff5722;
            margin-right: 0.5rem;
            font-size: 1.5rem;
        }
        .card-content {
            margin-bottom: 1rem;
        }
        .card-content p {
            font-size: 0.9rem;
            color: #bbb;
            margin: 0 0 0.5rem;
        }
        .file {
            background-color: #444;
            padding: 0.5rem;
            border-radius: 8px;
            color: #fff;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        blockquote {
            font-size: 0.9rem;
            color: #ddd;
            font-style: italic;
            border-left: 4px solid #555;
            padding-left: 0.5rem;
            margin: 0;
        }
        .card-footer {
            text-align: right;
        }
        .button {
            background-color: #007bff;
            color: #fff;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 0.9rem;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .button:hover {
            background-color: #0056b3;
            color: #fff;
        }
        .icon, .text {
  display: inline-block; /* Makes both elements align horizontally */
  margin-right: 10px; /* Adds space between them */
}
    </style>
</head>
<body>
    <div class="card">
        <div class="card-header">
        <h2 class="icon">🎯</h2>
        <h2 class="text">Opportunity</h2>
        </div>
        <div class="card-content">
            <p>Mengenrabatt-Klausel</p>
            <div class="file">Purchase_Agreement_BSH_02.pdf</div>
            <blockquote>"If the Purchaser buys 200 units of X in a single order, a discount of 50% on the total purchase value of the 500 units will apply."</blockquote>
        </div>
        <div class="card-footer">
            <a class="button">View Details</a>
        </div>
    </div>
</body>
</html>

    """

    # Use Streamlit to display the HTML
    return st.components.v1.html(html_code, height=500, scrolling=True)
