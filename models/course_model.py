# Python
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class Course(Base):
    __tablename__ = "tb_course"
    course_id = Column(Integer, primary_key=True)
    membership_id = Column(Integer, ForeignKey("tb_membership.membership_id"), nullable=True)
    video_list = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    active = Column(Boolean, nullable=False)
    content = Column(String, nullable=True)
    content_2 = Column(String, nullable=True)
    index = Column(String, nullable=True)
    learning = Column(String, nullable=True)
    interactive = Column(Boolean, nullable=False)
    product = Column(String, nullable=False)
    registration_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    update_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    membership = relationship("Membership", back_populates="course")
    video = relationship("Video", back_populates="course")