import streamlit as st
from utils import fetch_contracts, display_contracts
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer

# Check if the user is authenticated
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def extract_relevant_text(content, keyword, num_chars=9):
    # Case-insensitive search for the keyword
    keyword_position = content.lower().find(keyword.lower())
    if keyword_position != -1:
        # Extract a snippet of text around the found keyword
        start = max(keyword_position - num_chars // 2, 0)  # Start from a few characters before the keyword
        end = min(keyword_position + len(keyword) + num_chars // 2, len(content))  # End after the keyword
        relevant_text = content[start:end]
        return relevant_text
    else:
        return "Keyword not found in this contract."
    
    
    
def display_card(df):
    st.markdown("""
    <style>
        .card {
            padding: 15px;
            margin: 10px;
            transition: all 0.1s ease;
        }
        .card:hover {
            border: 2px solid #e14e47;  /* Streamlit red border color */
            cursor: pointer;
        }
    </style>
    """, unsafe_allow_html=True)
    
    N_cards_per_row = 2
    if not df.empty:
        for n_row, row in df.iterrows():
            i = n_row % N_cards_per_row
            if i == 0:
                st.write("---")  # Adds a horizontal line between rows
                cols = st.columns(N_cards_per_row, gap="large")
                
            # relevant_content = extract_relevant_text(row['content'], search_query)


            # Display each card
            with cols[i]:
                card_html = f"""
                <div class="card">
                    <h3>{row['file_name']}</h3>
                    <p><strong>Contract Value:</strong> {row['contract_value']}</p>
                    <p><strong>Item Purchased:</strong> {row['item_purchased']}</p>
                    <p><strong>Unit Price:</strong> {row['unit_price']}</p>
                    <hr>
                    <p><strong>Date Uploaded:</strong> {row.get('date_uploaded', 'N/A')}</p>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)

                # st.markdown(f"### {row['file_name']}")
                # st.write(f"**contract_value**: {row['contract_value']}")
                # st.write(f"**item_purchased**: {row['item_purchased']}")
                # st.write(f"**unit_price**: {row['unit_price']}")
                # # st.write(f"**Content (Snippet)**: ... {relevant_content}...")
                # st.write(f"---")
                # st.write(f"**Date Uploaded**: {row.get('date_uploaded', 'N/A')}")
                toggle_key = f"toggle-pdf-{n_row}"

                if toggle_key not in st.session_state:
                    st.session_state[toggle_key] = False 

                toggle_button = st.button(f"Show PDF {n_row}", key=f"toggle-button-{n_row}")
                if toggle_button:
                    st.session_state[toggle_key] = not st.session_state[toggle_key]  # Toggle state

                if st.session_state[toggle_key]:
                    output=display_contracts(row['file_name'])
                    pdf_viewer(output, key=f"pdf-viewer-{n_row}")
    return

def help_page():
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
    else:
        st.title("Intelligent Search")
        col1, col2 = st.columns(2)
        
        query_filter = {}
        with col1:
            user_input = st.text_area("Enter Keywords (separate with commas or spaces)", "")
            if user_input:
                keywords = [word.strip() for word in user_input.replace(",", " ").split() if word.strip()]
            else:
                keywords = []

            # Multi-select for choosing keywords from the list
            selected_keywords = st.multiselect("Select Keywords", options=keywords, default=keywords)

            # Build the query filter based on user input
                
            if selected_keywords:
                query_filter["$or"] = [
                {"content": {"$regex": keyword, "$options": "i"}} for keyword in selected_keywords
            ]
                
        with col2:
            col13=st.container()
            with col13:
                user_input2 = st.text_area("Enter Filename", "")
                if user_input2:
                    query_filter["file_name"] = {"$regex": user_input2, "$options": "i"}
            with col13:
                col111, coll23=st.columns(2)
                with col111:
                    options = ["Active", "Expired"]
                    selection = st.pills("Status", options, selection_mode="single")
                    current_date = pd.to_datetime("today")  # Get today's date
                    if selection == "Active":
                        query_filter["date_expiry"] = {"$gte": current_date.strftime("%Y-%m-%dT%H:%M:%S")}  # Expiration date >= today
                    elif selection == "Expired":
                        query_filter["date_expiry"] = {"$lt": current_date.strftime("%Y-%m-%dT%H:%M:%S")}
                    
                with coll23: 
                    min_value, max_value = st.slider(
                        "Select Contract Value Range",
                        min_value=0, 
                        max_value=1000,  # Adjust max value as needed
                        value=(0, 1000),  # Default range
                        step=100
                    )
                    query_filter["extracted_fields.contract_value"] = {
                        "$gte": min_value,  # Greater than or equal to min_value
                        "$lte": max_value   # Less than or equal to max_value
                    }
                
        
                
        # st.write("Query Filter:", query_filter)



        col3 = st.container()  
        with col3:
            if query_filter:
                # Fetch contracts that match the query
                results = fetch_contracts(query_filter)
                flat_data = []

                if results:
                    
                    for contract in results:
                        flat_contract = contract.copy()
                        flat_contract.update(contract['extracted_fields'])
                        del flat_contract['extracted_fields']  
                        flat_data.append(flat_contract)
                        
                    df = pd.DataFrame(flat_data)
                    display_card(df)
                    
                    
                else:
                    st.write("No results found.")
            else:
                st.write("Enter Something")
            
        


if __name__ == "__main__":
        help_page()
