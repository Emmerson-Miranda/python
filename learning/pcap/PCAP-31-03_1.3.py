"""
PCAP-31-03 1.3 – Generate random values using the random module

    functions: random(), seed(), choice(), sample()
"""

import random
import time


def main():
    print('random.randint(6, 10)   :', random.randint(6, 10))
    print('random.randrange(6, 10) :', random.randrange(6, 10))
    print('random.randrange(0, 1)  :', random.randrange(0, 1)) # always 0

    print('random.random              :', random.random())
    random.seed(12)
    print('random.random and seed(12) :', random.random())
    random.seed(12)
    print('random.random and seed(12) :', random.random())
    random.seed(12)
    print('random.random and seed(12) :', random.random())

    txt = 'Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.'
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    countries = ('Peru', 'Spain', 'UK', 'Brazil', 'France', 'Portugal')

    print('random.seed(time.time()) :', "Do that before choice and sample to get different values")

    print('random.choice(txt)       :', random.choice(txt))
    print('random.choice(numbers)   :', random.choice(numbers))
    print('random.choice(countries) :', random.choice(countries))

    print('random.sample(txt, k=3)       :', random.sample(txt, k=3))
    print('random.sample(numbers, k=3)   :', random.sample(numbers, k=3))
    print('random.sample(countries, k=3) :', random.sample(countries, k=3))


if __name__ == '__main__':
    main()
