"""
PCAP-31-03 5.2 – Embed lambda functions into the code

    lambdas: defining and using lambdas
    obj-defined functions taking lambdas as arguments
    functions: map(), filter()
"""
from functools import reduce

"""
https://www.simplilearn.com/tutorials/python-tutorial/map-in-python
https://www.w3schools.com/python/python_lambda.asp
https://www.w3schools.com/python/ref_func_filter.asp

Map
Syntax: map(function, iterables)
 function that works as an iterator to return a result after applying a function to every item of an 
 iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all 
 the iterable elements.
 Once the iteration is complete, it returns the map object. 
 
Filter
Syntax: filter(function, iterable) 
 The filter() function returns an iterator where the items are filtered through a function to test 
 if the item is accepted or not.
 
Lambda
Syntax: lambda arguments : expression
 Lambda functions are anonymous functions, i.e., without any name. The lambda function allows you 
 to define the function right inside the map() function.
 A lambda function can take any number of arguments, but can only have one expression.
 

"""

print(f'\nList comprehensions\n{"-" * 80}')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(f'fruits: {fruits}')


def square(x):
    return x * x


new_list = range(5)
square_list = list(map(square, new_list))
square_tuple = tuple(map(square, new_list))
print(f'list(map(square, {new_list})) : {square_list}')
print(f'tuple(map(square, {new_list})) : {square_tuple}')

square_list2 = list(map(lambda x: (x * x) + 1, new_list))
print(f'list(map(lambda x: x * x, {new_list})) : {square_list2}')


print(f'\nReduce\n{"-" * 80}')
r = reduce(lambda x, y: x + y, new_list)
print(f'reduce(lambda x, y: x + y, {new_list}) : ', r)

print(f'\nFilter\n{"-" * 80}')
ages = [5, 12, 17, 18, 24, 32]
print(f'list(filter(lambda x: x > 18, {ages}))   :', list(filter(lambda x: x > 18, ages)))
