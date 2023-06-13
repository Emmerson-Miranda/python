# https://realpython.com/python-lambda/#decorators
# allows adding a behavior to a function or a class
import sys
sys.path.insert(0, '../modules')
from utilities import print_header

def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps


def trace(f):

    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")


@trace
def decorated_fullname(name, surname):
    print(f"Full name: {name} {surname}")


print_header("01 decorator can be applied to a lambda function")
# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))

print_header("02 simple decorator")
decorated_function("hello world")

print_header("02 decorator can be applied to functions with multiple parametes")
decorated_fullname("Emmerson", "Miranda")
