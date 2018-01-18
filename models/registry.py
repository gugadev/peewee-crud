from peewee import *
from models.base import BaseModel
from models.student import Student
from models.group import Group


class Registry(BaseModel):
    student = ForeignKeyField(Student)
    group = ForeignKeyField(Group)