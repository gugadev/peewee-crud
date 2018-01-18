from peewee import *
from models.base import BaseModel


class Student(BaseModel):
    name = TextField()
    lastname = TextField()
    gender = FixedCharField(max_length=1)
    dni = FixedCharField(max_length=8, unique=True)
    address = TextField()
    phone = CharField(max_length=20)
    email = CharField(max_length=50)