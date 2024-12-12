#Function to handle CRUD operations for MongoDB
from models import Contract, Output
from datetime import datetime
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from extraction import process_contracts

load_dotenv()


def connect_to_db():
    MONGO_URI = os.getenv("MONGO_URI")
    mongodb_client = MongoClient(MONGO_URI,  tlsAllowInvalidCertificates=True)
    print("clinet is", MONGO_URI, mongodb_client)
    col = mongodb_client["LTC_DB"]["Contracts"]
    print("Connecting to", col)
    return mongodb_client, col

def close_mongodb_client(mongodb_client):
    mongodb_client.close()
    print("[INFO] MongoDB client closed.")

def upload_contract():
    contract_data = {
    "title": "Rental Agreement",
    "content": "This agreement is made between Tenant and Landlord...",
    "date_uploaded": str(datetime.now().isoformat())
    }
    
    extracted_fields={
        "rent": "$400",
        "deposit": "$500",
    }
    
    mongodb_client, contracts_collection=connect_to_db()
    output_instance = Output(**extracted_fields)
    contract = Contract(**contract_data, extracted_fields=output_instance)
    
    mongo_data = contract.model_dump(by_alias=True)
    insert_result=contracts_collection.insert_one(mongo_data)
    print(f"Document inserted with _id: {insert_result.inserted_id}")
    close_mongodb_client(mongodb_client)

def fetch_contracts(query=None, projection=None):
    """
    Fetch contracts from the MongoDB collection.
    
    Args:
        query (dict): A MongoDB query to filter results (default is None, which fetches all documents).
        projection (dict): A MongoDB projection to specify fields to return (default is None, which returns all fields).
    
    Returns:
        list: A list of documents matching the query.
    """
    if query is None:
        query = {}  # Default to fetching all documents
    
    try:
        mongodb_client, contracts_collection=connect_to_db()
        # Fetch documents based on query and projection
        results = contracts_collection.find(query, projection)
        print(results)
        close_mongodb_client(mongodb_client)
        return list(results)
    except Exception as e:
        print(f"An error occurred while fetching contracts: {e}")
        return []
    
    
# print(process_contracts(fetch_contracts()))