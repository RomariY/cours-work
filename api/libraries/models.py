import peewee

from api.base import database
from api.base.models import PeeweeGetterDict
from api.base.models import UUIDModel

TYPE_CHOICES = (
    (0, 'Draft'),
    (1, 'Published'),
    (2, 'Deleted')
)


class Library(UUIDModel):
    type = peewee.CharField(max_length=32, choices=TYPE_CHOICES)
    description = peewee.CharField(max_length=200)
    repo_link = peewee.CharField(max_length=50)

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


database.psql.create_tables([Library])
