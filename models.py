
from pydantic import BaseModel, Field
from datetime import datetime

class Output(BaseModel):
    rent: str = Field(description="Give me the monthly rental as in the contract")
    deposit: str = Field(description="Security deposit amount, as specified in the contract. This could also be referred to as "
        "a 'damage deposit' or 'initial deposit' depending on the text.")

class Contract(BaseModel):
    title: str = Field(description="Title or name of the contract", max_length=255)
    content: str = Field(description="Text content of the contract, extracted via OCR")
    date_uploaded: str = Field(default=str(datetime.now().isoformat()), description="Date the contract was uploaded")
    
    extracted_fields: Output = Field(
        default=None, description="Additional fields extracted from the contract text using an LLM"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Service Agreement",
                "content": "This agreement is made between Party A and Party B...",
                "date_uploaded": "2023-12-10T12:34:56",
                "extracted_fields": {
                    "rent": "1500 USD",
                    "deposit": "3000 USD"
                }
            }
        }