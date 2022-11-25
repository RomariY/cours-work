import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class GlossarySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str
    description: str


class GlossaryCreateSchema(BaseModel):
    name: str
    description: str


class GlossaryUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
