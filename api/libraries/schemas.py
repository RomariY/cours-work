import uuid
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl
from pydantic import Field


class S(str, Enum):
    group1 = 'Group1'
    group2 = 'Group2'
    group3 = "Group3"


class LibrarySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str
    type: S = S.group1
    description: str
    repo_link: HttpUrl


class LibraryCreateSchema(BaseModel):
    name: str
    type: S = S.group1
    description: str
    repo_link: HttpUrl


class LibraryUpdateSchema(BaseModel):
    name: Optional[str]
    type: Optional[S]
    description: Optional[str]
    repo_link: Optional[HttpUrl]
