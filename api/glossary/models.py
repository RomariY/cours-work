import peewee

from api.base.models import UUIDModel


class Glossary(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)

