import datetime
import uuid

import peewee
from playhouse.migrate import PostgresqlMigrator

import settings

psql = peewee.PostgresqlDatabase(
    database=settings.DATABASE,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.HOST,
    port=settings.PORT,
)
migrator = PostgresqlMigrator(psql)


class BaseModel(peewee.Model):
    """Parent for all app's models"""
    id = peewee.TextField(primary_key=True, default=uuid.uuid4())
    created = peewee.DateTimeField(default=datetime.datetime.now)
    modified = peewee.DateTimeField()

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        database = psql
