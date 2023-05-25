# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field


class MembershipBase(BaseModel):
    name: str = Field(
        ...,
        min_length=4,
        max_length=50,
        example="Nombre de membresía"
    )
    description: Optional[str] = Field(
        default=None,
        min_length=4,
        max_length=100,
        example="Esta es la descripción de la membresía."
    )

class Membership(MembershipBase):
    course_list: str = Field(
        ...,
        min_length=3,
        max_length=255,
        example="[1, 2]"
    )
    active: Optional[bool] = Field(
        default=1,
        example=1
    )
    cost: float = Field(
        ...,
        gt=0,
        le=100000,
        example=250.5
    )
    duration: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="6 meses"
    )
    to: str = Field(
        ...,
        min_length=4,
        max_length=50,
        example="Niños"
    )
    membership_url: Optional[str] = Field(
        default=None,
        min_length=7,
        max_length=255,
        example="https://www.humanium.org/es/wp-content/uploads/2021/02/shutterstock_1503499058-scaled.jpg"
    )