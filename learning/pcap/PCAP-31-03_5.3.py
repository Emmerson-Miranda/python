"""
PCAP-31-03 5.3 – Define and use closures

    closures: meaning and rationale
    defining and using closures

"""
import logging

"""
https://www.learnpython.org/en/Closures
https://www.scaler.com/topics/python/python-closure/
https://www.geeksforgeeks.org/python-closures/
https://docs.python.org/3/library/logging.html
https://www.programiz.com/python-programming/decorator

Closures
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
- Can be used to avoid the unnecessary use of class (When we have few functions in our code)
- Used to avoid the use of global scope.
- Used as callback functions, they provide some sort of data hiding. Helps us to reduce the use of global variables.
- Is a function object (function that behaves like an object)

Python Functions
Everything in Python is an object, even functions are objects. Functions are First Class citizens 
which means that functions can be treated similarly to objects:
- can be assigned to a variable i.e they can be referenced.
- can be passed as an argument to another function.
- can be returned from a function.

Decorators 
It allows programmers to modify the behavior of function or class. 
Is a function that takes in a function and returns it by adding some functionality.
Utilize nested functions (one function inside another)
A decorator is a callable that returns a callable
You can use the symbol @ to decorate a method
Multiple decorators can be chained (A function can have multiple decorator)
"""


print(f'\nSimple closure\n{"-" * 80}')


def divider(y):
    def divide(x):
        return x / y
    return divide


divider_by_2 = divider(2)
divider_by_5 = divider(5)

print('divider_by_2(20) : ', divider_by_2(20))
print('divider_by_5(20) : ', divider_by_5(20))


print(f'\nLambda closure\n{"-" * 80}')


def multiplier(n):
    return lambda a: a * n


my_doubler = multiplier(2)
my_tripler = multiplier(3)

print('my_doubler(11) : ', my_doubler(11))
print('my_tripler(11) : ', my_tripler(11))


print(f'\nClosure / Decorator\n{"-" * 80}')

# https://docs.python.org/3/library/logging.html#logrecord-attributes
FORMAT = '%(asctime)s %(levelno)s %(filename)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        return func(*args)
    return log_func


def add(x, y):
    return x+y


@logger
def multiply(x, y):
    return x * y


add_logger = logger(add)
print('callable(add_logger) :', callable(add_logger))
print('add(3, 3)            :', add(3, 3))
print('add_logger(3, 3)     :', add_logger(3, 3))
print('add_logger(4, 5)     :', add_logger(4, 5))
print('multiply(6, 5)       :', multiply(6, 5))

