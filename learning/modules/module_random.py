import random
from random import randrange
from random import choice

line = "-" * 80

print(line, "| 00.", line, sep="\n")
print(dir(random))

print(line, "| 01 randint - return a number between two number, including start and end number.", line, sep="\n")
print(random.randint(6,10))

print(line, "| 02 randrange ", line, sep="\n")
print(random.randrange(6,10))

print(line, "| 03 seed, random ", line, sep="\n")
print(random.random())
random.seed(12)
print(random.random())
random.seed(12)
print(random.random())

print(line, "| 04 randrange - Choose a random item from range(start, stop[, step]). ", line, sep="\n")
print(randrange(0, 1)) # always 0
print(randrange(0, 20, 5))

print(line, "| 05 choice. ", line, sep="\n")
name = 'Yahoo'
print(choice(name))

print(line, "| 06 sample. ", line, sep="\n")
countries = ('Peru', 'Spain', 'UK', 'Brazil', 'France')
print(random.sample(countries, k=3))

number = [1, 2, 3]
l = dir(number)
d = dir()
print("number", number)
print("l", l)
print("d", d)