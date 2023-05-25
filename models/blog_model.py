from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime

from database.database import Base

class Blog(Base):
    __tablename__ = "tb_blog"
    blog_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    sub_title = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)
    image = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    registration_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    update_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    questions = relationship("Question", back_populates="blog")


class Question(Base):
    __tablename__ = "tb_question"
    question_id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    question_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    active = Column(Integer, nullable=False)
    blog_id = Column(Integer, ForeignKey("tb_blog.blog_id"), nullable=False)
    blog = relationship("Blog", back_populates="questions")
    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "tb_answer"
    answer_id = Column(Integer, primary_key=True)
    answer = Column(Text, nullable=False)
    answer_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    active = Column(Integer, nullable=False)
    question_id = Column(Integer, ForeignKey("tb_question.question_id"), nullable=False)
    question = relationship("Question", back_populates="answers")
