from PyPDF2 import PdfReader  
import docx
import pandas as pd
from bson import ObjectId

def extract_text_from_file(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text()
        return extracted_text
    
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n\n".join([para.text for para in doc.paragraphs])
        return text
    
    else:
        return None
    
    
def process_contracts(contracts: list):
    # Flatten the data dynamically
    processed_data = []
    for contract in contracts:
        # Start with fixed fields
        flat_contract = {
            "_id": str(contract.get("_id", "")),  # Convert ObjectId to string
            "title": contract.get("title", ""),
            "content": contract.get("content", ""),
            "date_uploaded": contract.get("date_uploaded", "")
        }
        
        # Add dynamic extracted fields
        extracted_fields = contract.get("extracted_fields", {})
        for key, value in extracted_fields.items():
            flat_contract[key] = value
        
        processed_data.append(flat_contract)
    
    return pd.DataFrame(processed_data)
