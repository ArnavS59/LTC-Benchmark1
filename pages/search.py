import streamlit as st
from utils import fetch_contracts
import pandas as pd


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

def help_page():
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
    else:
        st.title("Intelligent Search")
        
    search_query = st.text_input("Search based on Keyword", "")
    
    query_filter = {
        "$or": [
            {"title": {"$regex": search_query, "$options": "i"}},
            {"content": {"$regex": search_query, "$options": "i"}}
        ]
    }
    
    if search_query:
        # Fetch contracts that match the query
        results = fetch_contracts(query_filter)
        flat_data = []

        if results:
            st.write(f"Showing results for '{search_query}':")
            
            for contract in results:
                flat_contract = contract.copy()
                flat_contract.update(contract['extracted_fields'])
                del flat_contract['extracted_fields']  
                flat_data.append(flat_contract)
                
            df = pd.DataFrame(flat_data)


            N_cards_per_row = 2
            if not df.empty:
                for n_row, row in df.iterrows():
                    i = n_row % N_cards_per_row
                    if i == 0:
                        st.write("---")  # Adds a horizontal line between rows
                        cols = st.columns(N_cards_per_row, gap="large")
                        
                    relevant_content = extract_relevant_text(row['content'], search_query)


                    # Display each card
                    with cols[i]:
                        st.markdown(f"### {row['title']}")
                        st.write(f"**Rent**: {row['rent']}")
                        st.write(f"**Deposit**: {row['deposit']}")
                        st.write(f"**Content (Snippet)**: ... {relevant_content}...")
                        st.write(f"---")
                        st.write(f"**Date Uploaded**: {row.get('date_uploaded', 'N/A')}")
            
        else:
            st.write("No results found.")
    else:
        st.write("Enter a keyword to search for contracts.")
        
        


if __name__ == "__main__":
    help_page()
