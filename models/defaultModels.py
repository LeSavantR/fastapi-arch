from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Base(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    time_now: Optional[datetime] = Field(default_factory=datetime.utcnow)
