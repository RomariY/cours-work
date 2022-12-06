import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic import Field

from api.base.models import BaseNameUnique
from api.glossary.models import Glossary


class GlossarySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)


class GlossaryCreateSchema(BaseModel, BaseNameUnique):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(GlossaryCreateSchema, cls).name_must_be_unique(value, Glossary)


class GlossaryUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    description: Optional[str] = Field(None, max_length=200)
