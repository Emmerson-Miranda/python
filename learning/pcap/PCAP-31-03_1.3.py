"""
PCAP-31-03 1.3 – Generate random values using the random module

    functions: random(), seed(), choice(), sample()
"""

import random
import time

def main():
    print('random.randint', random.randint(6, 10))
    print('random.randrange', random.randrange(6, 10))
    print('random.randrange', random.randrange(0, 1)) # always 0

    print('random.random', random.random())
    random.seed(12)
    print('random.random and seed', random.random())
    random.seed(12)
    print('random.random and seed', random.random())
    random.seed(12)
    print('random.random and seed', random.random())

    random.seed(time.time())  # do that before choice and sample to get different values

    txt = 'Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.'
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    countries = ('Peru', 'Spain', 'UK', 'Brazil', 'France', 'Portugal')

    print('random.choice txt', random.choice(txt))
    print('random.choice numbers', random.choice(numbers))
    print('random.choice countries', random.choice(countries))

    print('random.sample txt', random.sample(txt, k=3))
    print('random.sample numbers', random.sample(numbers, k=3))
    print('random.sample countries', random.sample(countries, k=3))


if __name__ == '__main__':
    main()
