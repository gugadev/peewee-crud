from models.student import Student
from models.course import Course
from models.group import Group
from models.registry import Registry
from models.score import Score


def students_count():
    return Student.select().count()


def courses_count():
    return Course.select().count()


def course_students_count(course):
    return (
        Registry
        .select()
        .join(Group)
        .join(Course)
        .where(Course.name == course)
        .count())


def course_high_score_count(course, base):
    return (
        Score
        .select()
        .join(Group)
        .join(Course)
        .where(Course.name == course, Score.score > base)
        .count())


def how_many_by_gender(gender):
    return (
        Student
        .select()
        .where(Student.gender == gender)
        .count())


def how_many_by_gender_and_ciurse(gender, course):
    return (
        Registry
        .select()
        .join(Group)
        .join(Course)
        .join(Student)
        .where(Student.gender == gender, Course.name == course)
        .count())


def create_student():
    Student.create(
        name="Valeria",
        lastname="Echevarría",
        address="Av. Vice #1084",
        gender="F",
        dni="49578120",
        phone="957831328",
        email="valechevarria94@gmail.com")
    s = Student.get(Student.dni == "49578120")
    return s.name


def update_student():
    rows = Student.update(name="Karina").where(Student.name=="Valeria").execute()
    return rows


def delete_student():
    rows = Student.delete().where(Student.name=="Karina").execute()
    return rows


"""
    Tests
"""


def test_students_count():
    assert students_count() == 3

def test_courses_count():
    assert courses_count() == 2

def test_algorithms_students_count():
    assert course_students_count("Algoritmos II") == 2

def test_structure_students_count():
    assert course_students_count("Estructura de datos") == 2

def test_course_high_score_count():
    assert course_high_score_count("Algoritmos II", 16) == 2

def test_how_many_by_gender():
    assert how_many_by_gender("F") == 2

def test_how_many_by_gender():
    assert how_many_by_gender("M") == 1

def test_create_student():
    assert create_student() == "Valeria"

def test_update_student():
    assert update_student() == 1 # rows affected

def test_delete_student():
    assert delete_student() == 1 # rows affected
