# Python
from sqlalchemy import Boolean, Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class Membership(Base):
    __tablename__ = "tb_membership"
    membership_id = Column(Integer, primary_key=True)
    course_list = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    active = Column(Boolean, nullable=False)
    cost = Column(DECIMAL, nullable=False)
    duration = Column(String, nullable=False)
    to = Column(String, nullable=False)
    membership_url = Column(String, nullable=True)
    registration_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    update_timestamp = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    course = relationship("Course", back_populates="membership")