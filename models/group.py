from peewee import *
from models.base import BaseModel
from models.course import Course


class Group(BaseModel):
    name = TextField()
    course = ForeignKeyField(Course)
    capacity = IntegerField()