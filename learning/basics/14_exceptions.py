#
# https://docs.python.org/3/tutorial/errors.html
#

line = "-" * 80

print(line, "| 01 try except", line, sep="\n")
try:
    print("TRY block running")
    y = 5 / 0
except ZeroDivisionError as myexception:
    print("ERROR objet: ", myexception)
else:
    print("ELSE There was no error")
finally:
    print("FINALLY of try catch")



print(line, "| 02 try except else finally", line, sep="\n")
try:
    print("TRY block running")
    y = 5 / 1
except ZeroDivisionError as myexception:
    print("ERROR objet: ", myexception)
else:
    print("ELSE was no error")
finally:
    print("FINALLY of try catch")

#When can we use the raise keyword?
#Inside the try block together with a named exception ,Inside the except block, but unnamed

print(line, "| 03 raise an exception", line, sep="\n")

def raise_exception(x):
    if x < 0:
        raise Exception("Sorry, number is below zero") 
    else:
        print(x, "The number is greater than zero")

try:
    raise_exception(1)
    raise_exception(-1)
except Exception as myexception:
    print(myexception)


print(line, "| 04 raise type error", line, sep="\n")
def raise_exception_type(x):
    if not type(x) is int:
      raise TypeError("Only integers are allowed") 
    else:
        print(x, "is a valid integer.")

try:
    raise_exception_type(1)
    raise_exception_type("hello")
except Exception as myexception:
    print(myexception)
