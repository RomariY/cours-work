import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class GlossarySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)


class GlossaryCreateSchema(BaseModel):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)


class GlossaryUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    description: Optional[str] = Field(None, max_length=200)
