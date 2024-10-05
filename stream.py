import streamlit as st
from ml import *

def display(col1, clauses):
    with col1:
        st.header("Contract Clauses")
        for idx, (clause, clause_type) in enumerate(clauses):
            st.write(f"**Clause {idx + 1}:**")
            st.write(clause)
            st.write(f"**Type:** {clause_type}")
            st.write("---")
        
def main():
    st.set_page_config(layout="wide")
    st.title('LTC Venture Dashboard')

    col1, col2 = st.columns([3, 1])
                
    with col2:
        st.header("Upload your contract file")
        # Create a file uploader in the second column
        uploaded_file = st.file_uploader("Choose a file")
        
        if uploaded_file:
                    # Extract text from the uploaded file
                    contract_text = extract_text_from_file(uploaded_file)
                    
                    if contract_text:
                        # Run clause identification on the contract text
                        clauses = identify_clauses(contract_text)
                        
                        # Display the extracted clauses in col1
                        display(col1, clauses)
                    else:
                        st.error("Unsupported file type or error reading the file.")
        
main()

