from pydantic import BaseModel , EmailStr , validator
from datetime import datetime
from typing import List
# Pydantic
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    email: EmailStr

    @validator('email')
    def email_must_contain_at_symbol(cls, v):
        if '@' not in v:
            raise ValueError('email must contain @ symbol')
        return v.lower()
class UserLogin(UserBase):
    password: str
    
class UserCreate(UserLogin):
    username: str
    password: str
    name: str
    midlename: str
    lastname: str
    birthdate: str  = Field(
        ...,
        min_length=4,
        max_length=50,
        example="23/12/1998"
    )
    phone: str
    role_id: int
    photo_id: int

class UserUpdate(UserLogin):
    username: str
    name: str
    midlename: str
    lastname: str
    birthdate: str = Field(
        ...,
        min_length=4,
        max_length=50,
        example="23/12/1998"
    )
    phone: str
    role_id: int
    photo_id: int
    is_activate: int

class User(UserBase):
    id: int
    username: str
    name: str
    midlename: str
    lastname: str
    birthdate: str
    phone: str
    is_activate: int
    role_id: int
    created_at: datetime
    updated_at: datetime

class EmailSchema(BaseModel):
    email: List[EmailStr]

    class Config:
        orm_mode = True
