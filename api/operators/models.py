import peewee

from api.base import database
from api.base.models import PeeweeGetterDict
from api.base.models import UUIDModel


class Operator(UUIDModel):
    name = peewee.CharField(max_length=32)
    syntax = peewee.CharField(max_length=200)
    example = peewee.TextField()

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


database.psql.create_tables([Operator])
