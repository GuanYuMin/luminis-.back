from pydantic import BaseModel , EmailStr , validator
from datetime import datetime


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
    birthdate: datetime
    phone: str
    role_id: int
    photo_id: int

class UserUpdate(UserLogin):
    username: str
    name: str
    midlename: str
    lastname: str
    birthdate: datetime
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
    birthdate: datetime
    phone: str
    is_activate: int
    role_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
