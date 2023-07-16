"""
PCAP-31-03 5.1 – Build complex lists using list comprehension

    list comprehensions: the if operator, nested comprehensions

"""

"""
https://www.w3schools.com/python/python_lists_comprehension.asp
https://realpython.com/list-comprehension-python/

List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Syntax: newlist = [expression for item in iterable if condition == True]
- list comprehensions can also be used for mapping and filtering.
- List comprehensions are also more declarative than loops
- They might make your code run more slowly or use more memory.


Nested Comprehensions
Comprehensions can be nested to create combinations of lists, dictionaries, and sets within a collection.

"""

print(f'List comprehensions\n{"-" * 80}')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(f'fruits: {fruits}')
newlist = [x for x in fruits if "a" in x]
print(f'[x for x in fruits if "a" in x] : {newlist}')

newlist = [x if x != "banana" else "orange" for x in fruits]
print(f'[x if x != "banana" else "orange" for x in fruits] : {newlist}')

newlist = [x for x in range(10) if x < 5]
print(f'[x for x in range(10) if x < 5] : {newlist}')


def square(x):
    return x * x


square_list = list(map(square, newlist))
print(f'list(map(square, {newlist})) : {square_list}')

square_list_comprenhension = [x * x for x in newlist]
print(f'[x * x for x in {newlist}] : {square_list_comprenhension}')
print('')

print(f'Dictionary comprehensions\n{"-" * 80}')
ob, cb = '{', '}'
squares = {i: i * i for i in newlist}
print(f'{ob}i: i * i for i in {newlist}{cb} : {squares}')

# Nested Comprehensions
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(3)] for city in cities}
print(f'{ob}city: [0 for _ in range(7)] for city in {cities}{cb} : {temps}')

matrix = [[(x * 10) + i for i in range(3)] for x in range(6)]
print(f'[[(x * 10) + i for i in range(3)] for x in range(6)] : {matrix}')

matrix = [{x: [(x * 10) + i for i in range(3)]} for x in range(6)]
print(f'[{ob}x: [(x * 10) + i for i in range(3)]{cb} for x in range(6)] : {matrix}')
