from contextvars import ContextVar

import peewee
from fastapi import Depends
from playhouse.migrate import PostgresqlMigrator

import settings

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


psql = peewee.PostgresqlDatabase(
    database=settings.DATABASE,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.HOST,
    port=settings.PORT,
)
migrator = PostgresqlMigrator(psql)
psql._state = PeeweeConnectionState()


async def reset_db_state():
    psql._state._state.set(db_state_default.copy())
    psql._state.reset()


def get_db(psql_state=Depends(reset_db_state)):
    try:
        psql.connect()
        yield
    finally:
        if not psql.is_closed():
            psql.close()