from datetime import datetime
import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean, Enum, UUID
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

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
    __tablename__ = 'sections'
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


class ContentBlock(Base):
    """ PASS """
    __tablename__ = 'content_blocks'
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
    type = Column(
        Enum(ContentType)
    )
    url = Column(
        URLType, nullable=True
    )
    content = Column(
        Text, nullable=True
    )
    section_id = Column(
        Integer, ForeignKey('sections.id'),
        nullable=False
    )

    # Relations
    section = relationship(
        'Section', back_populates='content_blocks'
    )
    complete_content_blocks = relationship(
        'CompleteContentBlock', back_populates='content_blocks'
    )


class StudentCourse(Base):
    """  """
    __tablename__ = 'student_courses'
    id = Column(
        Integer, primary_key=True,
        index=True
    )
    student_id = Column(
        UUID, ForeignKey('users.id'),
        nullable=False
    )
    course_id = Column(
        Integer, ForeignKey('users.id'),
        nullable=False
    )
    completed = Column(
        Boolean, default=False
    )

    # Relations
    student = relationship(
        User, back_populates='student_courses'
    )
    course = relationship(
        'Course', back_populates='student_courses'
    )


class CompletedContentBlock(Base):
    """  """
    student_id = Column(
        UUID, ForeignKey('users.id'),
        nullable=False
    )
    content_block_id = Column(
        Integer, ForeignKey('content_blocks.id'),
        nullable=False
    )
