from uuid import uuid4
from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, UUID, DateTime
from sqlalchemy.orm import relationship

from database.db_setup import _Base


class Base(_Base):
    """
        Base Model:
        -
    """
    __abstract__ = True
    id = Column(
        UUID(), default=uuid4,
        name='ID', index=True,
        primary_key=True
    )
