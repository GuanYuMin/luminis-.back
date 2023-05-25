from pydantic import BaseModel
from datetime import datetime


class OpenpayBase(BaseModel):
    card_number: str
    holder_name: str
    expiration_year: str
    expiration_month: str
    cvv2: str
    device_session_id: str
    token_id: str
    is_activate: bool

class OpenpayCreate(OpenpayBase):
    pass

class OpenpayUpdate(OpenpayBase):
    pass

class Openpay(OpenpayBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True