# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field


class VideoBase(BaseModel):
    name: str = Field(
        ...,
        min_length=4,
        max_length=50,
        example="Guía contra el bulliyng"
    )
    description: Optional[str] = Field(
        default=None,
        min_length=4,
        max_length=100,
        example="Para ayudar a combatir el acoso en escolares."
    )

class Video(VideoBase):
    course_id: Optional[int] = Field(
        default=None,
        gt=0,
        le=100000,
        example=1
    )
    type: str = Field(
        ...,
        min_length=4,
        max_length=50,
        example="Digital"
    )
    cost: float = Field(
        ...,
        gt=0,
        le=100000,
        example=250.5
    )
    video_url: str = Field(
        ...,
        min_length=7,
        max_length=255,
        example="https://www.humanium.org/es/wp-content/uploads/2021/02/shutterstock_1503499058-scaled.jpg"
    )