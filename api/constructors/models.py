import peewee
from api.base.models import BaseModel


class Constructor(BaseModel):
    name = peewee.CharField(max_length=32)
    description = peewee.TextField()
    params = peewee.

