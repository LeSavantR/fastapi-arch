from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from db.db_setup import _Base

class Base(_Base):
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
