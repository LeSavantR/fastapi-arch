from typing import Optional

from models.defaultModels import Base


class User(Base):
    email: str
    is_active: Optional[bool] = True
    bio: Optional[str]
