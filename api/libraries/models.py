import peewee
from playhouse.migrate import migrate

from api.base import database
from api.base.database import migrator
from api.base.models import PeeweeGetterDict
from api.base.models import UUIDModel

TYPE_CHOICES = (
    (0, 'Group1'),
    (1, 'Group2'),
    (2, 'Group3')
)


class Library(UUIDModel):
    name = peewee.CharField(max_length=50, null=True)
    type = peewee.CharField(max_length=32, choices=TYPE_CHOICES)
    description = peewee.CharField(max_length=200)
    repo_link = peewee.CharField(max_length=200)

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


database.psql.create_tables([Library])