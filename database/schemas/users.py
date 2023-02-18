import enum

from sqlalchemy import Boolean, Column, Enum, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.schemas.base import Base


class Role(enum.Enum):
    """ Roles """
    admin = 1
    coord = 2
    emprs = 3
    medics = 4
    enferm = 5


class User(Base):
    """
        User Model:
        -
    """
    __tablename__ = 'users'
    email = Column(
        String(200), unique=True,
        nullable=False, index=True
    )
    role = Column(
        Enum(Role)
    )

    profile = relationship(
        'Profile', back_populates='owner',
        uselist=False
    )


class Profile(Base):
    """
        Profile Model:
        -
    """
    __tablename__ = 'profiles'
    first_name = Column(
        String(150), nullable=False
    )
    last_name = Column(
        String(150), nullable=False
    )
    bio = Column(
        Text, nullable=True
    )
    is_active = Column(
        Boolean, default=False,
    )
    user_id = Column(
        String(100), ForeignKey('users.id'),
        nullable=False,
    )

    owner = relationship(
        'User', back_populates='profile'
    )
