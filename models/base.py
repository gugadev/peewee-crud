from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


class BaseModel(Model):
    class Meta:
        database = SqliteExtDatabase("data.db")
