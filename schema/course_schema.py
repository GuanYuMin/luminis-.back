# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    name: str=Field(
        ...,
        min_length=4,
        max_length=50,
        example="Curso contra la depresión"
    )
    description: Optional[str]=Field(
        default=None,
        min_length=4,
        max_length=100,
        example="Para ayudar a combatir la depresión."
    )

class Course(CourseBase):
    membership_id: Optional[int] = Field(
        default=None,
        gt=0,
        le=100000,
        example=1
    )
    video_list: str = Field(
        ...,
        min_length=3,
        max_length=255,
        example="[1, 2]"
    )
    active: Optional[bool] = Field(
        default=1,
        example=1
    )
    content: Optional[str]=Field(
        default=None,
        min_length=4,
        max_length=100,
        example="Content1"
    )
    content_2: Optional[str]=Field(
        default=None,
        min_length=4,
        max_length=100,
        example="Content2"
    )
    index: Optional[str]=Field(
        default=None,
        min_length=3,
        example="[1, 2]"
    )
    learning: Optional[str]=Field(
        default=None,
        min_length=3,
        example="[1, 2]"
    )
    interactive: Optional[bool] = Field(
        default=1,
        example=1
    )
    product: str=Field(
        ...,
        min_length=4,
        max_length=100,
        example="Product1"
    )