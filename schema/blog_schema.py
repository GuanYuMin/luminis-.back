from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    sub_title: Optional[str]
    content: str
    image: str
    author: str
    active: int
    category: str


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    id: int
    registration_timestamp: datetime
    update_date: datetime
    questions: List["Question"] = []

    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    question: str
    active: int
    blog_id: int

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    pass

class QuestionDelete(QuestionBase):
    pass
class Question(QuestionBase):
    question_id: int
    question_timestamp: datetime
    blog: Blog
    answers: List["Answer"] = []

    class Config:
        orm_mode = True
    

class AnswerBase(BaseModel):
    answer: str
    active: int
    question_id: int

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    pass

class Answer(AnswerBase):
    answer_id: int
    answer_timestamp: datetime
    question: Question

    class Config:
        orm_mode = True
