from peewee import *
from models.base import BaseModel
from models.group import Group
from models.student import Student


class Score(BaseModel):
    group = ForeignKeyField(Group)
    student = ForeignKeyField(Student)
    score = DecimalField()