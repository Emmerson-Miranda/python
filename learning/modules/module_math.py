#
# https://docs.python.org/3/tutorial/stdlib.html#mathematics
#

import math
from math import pi as mypi

line = "-" * 80
print(line, "| Module" + __name__, line, sep="\n")


print(line, "| 01 import, from, pi", line, sep="\n")
f = math.cos(math.pi / 4)
print("math.cos", f)
print("math.pi", math.pi)
print("mypi", mypi)

"""

hypot(x1, x2, x3, ..,xn) => 

factorial(x) => returns the factorial of a number, it only accepts positive integers. The factorial of a number is the sum of the multiplication, of all the whole numbers, from our specified number down to 1. E.x the factorial of 4 would be 4 x 3 x 2 x 1 = 24
"""

print(line, "| 02 ceil - rounds the number x up to the nearest integer", line, sep="\n")
print(math.ceil(4.4))
print(math.ceil(4.5))
print(math.ceil(4.6))

print(line, "| 03 floor - rounds the number x down to the nearest integer", line, sep="\n")
print(math.floor(4.4))
print(math.floor(4.5))
print(math.floor(4.6))

print(line, "| 04 trunc - the value of x truncated to an integer", line, sep="\n")
print(math.trunc(4.4))
print(math.trunc(4.5))
print(math.trunc(4.6))

print(line, "| 05 pow => returns the value of (x ** y) ", line, sep="\n")
print(math.pow(2,2))
print(math.pow(2,3))
print(math.pow(2,4))

print(line, "| 06 hypot => calculates the Euclidean form ", line, sep="\n")
#calculates the Euclidean form. For n-dimensional cases, the coordinates passed are assumed to be like (x1, x2, x3, …, xn). It is calculated by sqrt(x1*x1 + x2*x2 +x3*x3 …. xn*xn).
print(math.hypot(9,12))
