
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional

class Output(BaseModel):
    contract_value: float = Field(description="Value of the total contract")
    item_purchased: str = Field(description="Unit items purchased")
    unit_price: float = Field(description="Unit price of an item")
    payment_terms: str = Field(description="Payement terms")
    penalties: str = Field(description="Penalties")
    delivery_schedule : str = Field(description="Delivery schedule")
    contract_type: str = Field(description="Type of contract")
    department: str = Field(description="Department")

    
class Contract(BaseModel):
    title: str = Field(description="Title or name of the contract", max_length=255)
    content: str = Field(description="Text content of the contract, extracted via OCR")
    date_uploaded: Optional[str] = Field(default=str(datetime.now().isoformat()), description="Date the contract was uploaded")
    date_expiry: str = Field(default=str((datetime.now()+ timedelta(days=12)).isoformat()),description="Date the contract expiry")    
    extracted_fields: Output = Field(
        default=None, description="Additional fields extracted from the contract text using an LLM"
    )
    pdf_data: Optional[bytes] = Field(default=None, description="Data of pdf")
    file_name: str = Field(default=None, description="File name of the contract")