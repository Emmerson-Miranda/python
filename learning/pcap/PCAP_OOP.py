from datetime import datetime


class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__created_at = datetime.now()

    def __str__(self):
        return f'Person: {self.surname}, {self.name} is {self.age} years old.'

    def public_method(self):
        print(f"I'm public {self.name}")

    def _private_method(self):
        print(f"I'm private {self.name}")

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, fullname):
        name, surname = fullname.split()
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        self.name = None
        self.surname = None


class Student(Person):

    __counter = 0

    def __init__(self, name, surname, grade, age):
        super().__init__(name, surname, age)
        self.grade = grade
        self.__registered_at = datetime.now()
        Student.__counter += 1
        print("Creating object of", self.__class__.__name__, "counter", self.__class__.__counter)

    def __repr__(self):
        return repr((self.name, self.surname, self.grade, self.age))

    def __str__(self):
        sup = super().__str__()
        return f'Student: {sup} Grade {self.grade}'

    def __del__(self):
        print("Destroying object of", self.__class__.__name__, "counter", self.__class__.__counter)
        self.__class__.__counter -= 1

    @property
    def fullname(self):
        return super().fullname.upper()

    def info(self):
        return f'Name: {__name__}, Module: {self.__module__} , Bases: {Student.__bases__}, File: {__file__}'

