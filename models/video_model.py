# Python
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class Video(Base):
    __tablename__ = "tb_video"
    video_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("tb_course.course_id"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    type = Column(String, nullable=False)
    cost = Column(DECIMAL, nullable=False)
    video_url = Column(String, nullable=False)
    registration_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    update_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    course = relationship("Course", back_populates="video")