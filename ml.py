from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from io import StringIO

# Import libraries to handle different file types
from PyPDF2 import PdfReader  # Updated to PdfReader
import docx

import re

class_mapping = {
    0: "Termination Clause",
    1: "Payment Clause",
    2: "Confidentiality Clause",
    3: "Liability Clause",
    4: "Governing Law Clause",
    5: "Indemnity Clause",
    6: "Delivery Clause",
    # Add additional mappings as necessary
}

def identify_clauses(text):
    # Load LegalBERT tokenizer and model (pre-trained)
    tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("nlpaueb/legal-bert-base-uncased")
    
    # Use regex to find potential clauses based on common legal phrasing
    potential_clauses = re.split(r'\n\s*\n|(?<=\.)(?=\s*[A-Z])', text)  # Split based on double newlines or end of sentence followed by capital letter
    
    clause_results = []
    for clause in potential_clauses:
        if len(clause.strip()) > 0:  # Ignore empty clauses
            inputs = tokenizer(clause, return_tensors="pt", truncation=True, padding=True)
            outputs = model(**inputs)
            probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
            
            # Here we can add logic to interpret the outputs based on the model's task
            predicted_class = torch.argmax(probabilities, dim=-1).item()
            
            # Map predicted class to actual clause type (if you have a mapping)
            clause_type = class_mapping[predicted_class]  # assuming class_mapping is defined
            clause_results.append((clause.strip(), clause_type))
    
    return clause_results

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)  # Updated to PdfReader
        text = ""
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]  # Updated to use pages[] instead of getPage()
            text += page.extract_text()
        return text
    
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n\n".join([para.text for para in doc.paragraphs])
        return text
    
    elif uploaded_file.name.endswith(".txt"):
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    
    else:
        return None