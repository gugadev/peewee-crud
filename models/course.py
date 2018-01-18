from peewee import *
from models.base import BaseModel


class Course(BaseModel):
    name = TextField()
    credits = IntegerField()