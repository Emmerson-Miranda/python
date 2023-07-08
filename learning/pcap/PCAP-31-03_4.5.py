"""
PCAP-31-03 4.5 – Build a class hierarchy using inheritance

    single and multiple inheritance
    the isinstance() function
    overriding
    operators:
    not is
    , is
    polymorphism
    overriding the __str__() method
    diamonds

"""

"""
Polymorphism
https://www.digitalocean.com/community/tutorials/how-to-apply-polymorphism-to-classes-in-python-3#what-is-polymorphism
https://ellibrodepython.com/polimorfismo-en-programacion

Polymorphism can be carried out through inheritance, with subclasses making use of base class methods or overriding them.
Python’s duck typing, a special case of dynamic typing, uses techniques characteristic of polymorphism, 
including late binding and dynamic dispatch. 
The term “duck typing” is derived from a quote of writer James Whitcomb Riley: 
“When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.
That is to say, you check whether the object quacks like a duck and walks like a duck rather than 
asking whether the object is a duck.

Polymorphism, we can have different classes with methods that have the same name and parameters but different 
implementation without require interfaces like in java.



Diamonds
https://realpython.com/inheritance-composition-python/
https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem
    
Class A
Class B(A), C(A)
Clss D(B, C)
"""


class NumericCalc:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add(self):
        return f'Addition is:  {self._x + self._y}'


class OtherClass:

    def add(self):
        return f'This method does something different, class {self.__class__.__name__}'


class Dog:

    def greetings(self):
        return f'gruff gruff from {self.__class__.__name__}'


class Cat:

    def greetings(self):
        return f'miau miau from {self.__class__.__name__}'


if __name__ == '__main__':
    nc = NumericCalc(4, 6)
    oc = OtherClass()

    for i, obj in enumerate((nc, oc)):
        print(f'loop {i} : {obj.add()}')

    def run(o):
        return o.greetings()

    animal = Cat()
    print(f'from method: {run(animal)}')
    animal = Dog()
    print(f'from method: {run(animal)}')
