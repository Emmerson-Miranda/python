# https://realpython.com/python-lambda/
# https://www.w3schools.com/python/python_lambda.asp
# Python lambdas are little, anonymous functions, subject to a more restrictive
# but more concise syntax than regular Python functions.
# A lambda function can take any number of arguments, but can only have one expression.

from functools import reduce
from learning.modules.utilities import print_header
#import sys
#sys.path.insert(0, '../modules')
#from utilities import print_header

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

print_header("08 sorting with lambda")
books = [
    {'year': 1955, 'name': 'Pedro paramo'},
    {'year': 1265, 'name': 'Divina comedia'},
    {'year': 1967, 'name': 'Cien años de soledad'},
    {'year': 1952, 'name': 'El viejo y el mar'},
]

sorted_books = sorted(books, key=lambda x: x['year'])
print("Before order:", books)
print("After order :", sorted_books)

animal_list = ['cat', 'dog', 'cow', 'bird', 'rabbit', 'snake']
animal_list.sort()
print('Animals', animal_list)

u_animals = list(map(lambda a: a.upper(), animal_list))
print('Uppercase Animals as lambda:', u_animals)
u_animals = [e.upper() for e in animal_list]
print('Uppercase Animals as List comprehension:', u_animals)

a_animals = list(filter(lambda e: 'a' in e, animal_list))
print('Animals with a:', a_animals)

print('Reduced', reduce(lambda acc, e: f'{acc} | {e}', animal_list))

