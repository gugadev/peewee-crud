from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from models.student import Student
from models.course import Course
from models.group import Group
from models.registry import Registry
from models.score import Score


db = SqliteExtDatabase("data.db")


"""
    Recreate the tables
"""

db.connect()
db.drop_tables([Student, Course, Group, Registry, Score])
db.create_tables([Student, Course, Group, Registry, Score])


"""
    Populate database
"""


mia = Student.create(
    name="Mía",
    lastname="Figueroa",
    gender="F",
    dni="50348343",
    address="Jr. Cuzco #756",
    phone="946485322",
    email="miafigueroa9@gmail.com"
)
danna = Student.create(
    name="Danna",
    lastname="Valenzuela",
    gender="F",
    dni="49357820",
    address="Av. Progreso #1862",
    phone="922785464",
    email="danna.vzuela@yahoo.com"
)
brian = Student.create(
    name="Brian",
    lastname="Huilca",
    gender="M",
    dni="50274566",
    address="Clle. Callao #380",
    phone="94678215",
    email="sbrian_huilca95@outlook.com"
)
datos = Course.create(
    name="Estructura de datos",
    credits=4
)
algoritmos = Course.create(
    name="Algoritmos II",
    credits=5
)
dat_group = Group.create(
    course=datos,
    name="GDAT01",
    capacity=40
)
alg_group = Group.create(
    course=algoritmos,
    name="GALG01",
    capacity=45
)
Registry.create(
    group=dat_group,
    student=mia
)
Registry.create(
    group=dat_group,
    student=danna
)
Registry.create(
    group=alg_group,
    student=brian
)
Registry.create(
    group=alg_group,
    student=danna
)
Score.create(
    group=dat_group,
    student=mia,
    score=16.85
)
Score.create(
    group=dat_group,
    student=danna,
    score=15.93
)
Score.create(
    group=alg_group,
    student=danna,
    score=17.29
)
Score.create(
    group=alg_group,
    student=brian,
    score=16.51
)

db.close()