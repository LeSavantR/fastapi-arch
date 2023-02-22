from datetime import datetime
import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.util import URLType

from database.schemas.base import Base
from database.schemas.users import User
from database.schemas.mixins import Timestamp


class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assigment = 3


class Course(Timestamp, Base):
    """  """
    __tablename__ = 'courses'
    id = Column(
        Integer, primary_key=True,
        index=True
    )
    title = Column(
        String(200), nullable=False
    )
    description = Column(
        Text, nullable=True
    )
    user_id = Column(
        Integer, ForeignKey('users.id'),
        nullable=False
    )

    # Relations
    create_by = relationship(User)
    sections = relationship(
        'Section',
        back_populates='course',
        uselist=False
    )
    students_courses = relationship(
        'StudentCourse',
        back_populates='course'
    )


class Section(Base):
    """  """
    id = Column(
        Integer, primary_key=True,
        index=True
    )
    title = Column(
        String(200), nullable=False
    )
    description = Column(
        Text, nullable=True
    )
    course_id = Column(
        Integer, ForeignKey('courses.id'),
        nullable=False
    )

    # Relations
    course = relationship(
        'Course', back_populates='section'
    )
    content_blocks = relationship(
        'ContentBlock', back_populates='section'
    )
