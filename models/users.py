from typing import Optional

from pydantic import Field, EmailStr

from models.defaultModels import Base


class User(Base):
    """
        User Model:
        - Email.
        - Is_Active.
        - Bio.
    """
    email: str = Field(
        title='Email',
    )
    is_active: Optional[bool] = Field(
        title='Is Active',
        default=True
    )
    bio: Optional[str] = Field(
        title='Bio'
    )
