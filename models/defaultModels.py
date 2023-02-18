from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import Field, BaseModel


class Base(BaseModel):
    """
        Base Model:
        - ID.
        - Created_At.
    """
    id: UUID = Field(
        title='ID:',
        default_factory=uuid4
    )
    created_at: Optional[datetime] = Field(
        title='Created At:',
        default_factory=datetime.utcnow
    )
