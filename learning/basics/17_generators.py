# https://wiki.python.org/moin/Generators

import sys
sys.path.insert(0, '../modules')
from utilities import print_header

# range generator
print_header("01 range generation")
li = [i for i in range(4)]
print(li)

# Generation pattern
print_header("02 generator pattern")


class GeneratorPattern:

    def __init__(self, min, max):
        self._min = ord(min)
        self._max = ord(max)
        self._current = ord(min) - 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self._current < self._max:
            self._current += 1
            return chr(self._current)
        raise StopIteration()


seed = GeneratorPattern('T', 'h')
list0 = [char for char in seed]
print(list0)

# list comprehension
print_header("03 list comprehension")
list2 = [chr(x) for x in range(ord('T'), ord('h'))]
print(list2)

# list comprehension
print_header("04 list comprehension - using list and parenthesis")
list3 = list(chr(x) for x in range(ord('T'), ord('h')) )
print(list3)


print_header("05 generator that yields items instead of returning a list")


def generator_fn(minchr, maxchr):
    min = ord(minchr)
    max = ord(maxchr)
    while min <= max:
        yield chr(min)
        min += 1


list4 = [e for e in generator_fn('T', 'h')]
print(list4)

# a generator that yields items instead of returning a list
print_header("06 simple generator that yields items instead of returning a list")


def firstn(n):
     num = 0
     while num < n:
         yield num
         num += 1


sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

