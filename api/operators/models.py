import peewee

from api.base.models import UUIDModel


class Operator(UUIDModel):
    name = peewee.CharField(max_length=32)
    syntax = peewee.CharField(max_length=200)
    example = peewee.TextField()
