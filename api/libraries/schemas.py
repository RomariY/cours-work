import uuid
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl
from pydantic import Field


class S(str, Enum):
    draft = 'Draft'
    published = 'Published'
    deleted = "Deleted"


class LibrarySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    type: S
    description: str
    repo_link: HttpUrl


class LibraryCreateSchema(BaseModel):
    type: S
    description: str
    repo_link: HttpUrl


class LibraryUpdateSchema(BaseModel):
    type: Optional[S]
    description: Optional[str]
    repo_link: Optional[HttpUrl]
