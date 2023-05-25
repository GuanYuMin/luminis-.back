from pydantic import BaseModel
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    description: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass
class Role(RoleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
