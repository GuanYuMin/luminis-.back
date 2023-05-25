from pydantic import BaseModel
from datetime import datetime


class PhotoBase(BaseModel):
    photo_name: str
    photo_url: str
    is_activate: bool
    
class PhotoCreate(PhotoBase):
    pass

class PhotoUpdate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        