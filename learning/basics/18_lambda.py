# https://realpython.com/python-lambda/

import sys
sys.path.insert(0, '../modules')
from utilities import print_header

print_header("01 named lambda with two parameters")
named_lambda = (lambda x, y, z: x + y + z)
result = named_lambda(1, 2, 3)
print("The result is ", result)

print_header("02 inline lambda with two arguments")
result = (lambda x, y, z=3: x + y + z)(1, 2)
print("The result is ", result)

print_header("03 inline lambda with named parameters and default values")
result = (lambda x, y, z=3: x + y + z)(1, y=2)
print("The result is ", result)

print_header("04 inline lambda with dynamic arguments")
result = (lambda *args: sum(args))(1, 2, 3, 4)
print("The result is ", result)

print_header("05 inline lambda with dynamic named arguments")
result = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print("The result is ", result)

print_header("06 inline lambda inside filter")
even = list(filter(lambda x : x % 2 != 0, range(10)))
print(even)

print_header("06 inline lambda inside map")
doubles = list(map(lambda x : x * 2, range(10)))
print(doubles)

print_header("07 filtering numbers")
elems = [1, "hello", 0.5, "world", 10.0, "\n"]
numbers = list(filter(lambda e: isinstance(e, int) or isinstance(e, float), elems))
print(numbers)

print_header("08 sorting books")
books = [
    {'year': 1955, 'name': 'Pedro paramo'},
    {'year': 1265, 'name': 'Divina comedia'},
    {'year': 1967, 'name': 'Cien años de soledad'},
    {'year': 1952, 'name': 'El viejo y el mar'},
]

sorted_books = sorted(books, key=lambda x: x['year'])
print("Before order:", books)
print("After order :", sorted_books)

