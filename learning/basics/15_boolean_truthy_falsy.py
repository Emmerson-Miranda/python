# https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/
# we can import modules in different locations using sys
import sys
sys.path.insert(0, '../modules')
from utilities import print_header


"""
Truthy values (By default, an object is considered true.)

    Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
    Numeric values that are not zero.
    True
    By default, an object is considered true unless its class defines either a __bool__() method that returns False
    or a __len__() method that returns zero, when called with the object.

Falsy Values (By default, an object is considered false.)

Sequences and Collections:

    Empty lists []
    Empty tuples ()
    Empty dictionaries {}
    Empty sets set()
    Empty strings ""
    Empty ranges range(0)

Numbers

    Zero of any numeric type.
    Integer: 0
    Float: 0.0
    Complex: 0j

Constants

    None
    False
"""

a, b, c, d, e = 1, 22, 333, 0, -23
empty_collection, non_empty_collection = [], [1, "", 3.0]
empty_tuple, non_empty_tuple = (), (1, 2, 3)
empty_string, non_empty_string = "", "some value"
empty_dictionary, non_empty_dictionary = {}, {a: 1, b: 2}
empty_range, non_empty_range = range(0), range(1, 5)

print_header("01 truthy")
print("Any non zero         bool value: ", bool(a), bool(b), bool(c), bool(e))
print("Collection with data bool value: ", bool(non_empty_collection))
print("Tuple      with data bool value: ", bool(non_empty_tuple))
print("String     with data bool value: ", bool(non_empty_string))
print("Dictionary with data bool value: ", bool(non_empty_dictionary))
print("Range      with data bool value: ", bool(non_empty_range))

print_header("02 falsy")
print("Number 0         bool value:", bool(d))
print("Empty Collection bool value:", bool(empty_collection))
print("Empty Tuple      bool value:", bool(empty_tuple))
print("Empty String     bool value:", bool(empty_string))
print("Empty Dictionary bool value:", bool(empty_dictionary))
print("Empty Range      bool value:", bool(empty_range))

print_header("03 __bool__ function in a class")


class EmptyObject:

    def __init__(self):
        pass


empty =  EmptyObject()
print("Object default boolean value is", bool(empty))


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return self._name

    def __bool__(self):
        return self._age > 20


def buy_alcohol(person):
    if person:
        print(person, "Can buy alcohol.")
    else:
        print(person, "Not allowed to buy alcohol")


dedalo = Person("Dedalo", 30)
icaro = Person("Icaro", 10)

buy_alcohol(icaro)
buy_alcohol(dedalo)

