"""
PCAP-31-03 4.1 – Understand the Object-Oriented approach

    ideas and notions: class, object, property, method, encapsulation,
    inheritance, superclass, subclass, identifying class components

"""
import PCAP_OOP

"""

Class
Classes are like a blueprint or a prototype that you can define to use to create objects. 
This defines a set of attributes that will characterize any object that is instantiated from this class.

Object 
An instance of a class. This is the realized version of the class, 
where the class is manifested in the program.

Property
https://realpython.com/python-property/
Functions that behave and are used like a field/attribute. 
Can be used to: validate values, create computed attributes, logging attribute access.
Properties are arguably the most popular way to create managed attributes quickly and in the purest Pythonic style.
A property can be to r/json_obj2, r, json_obj2 and/or deletion.

Method
Methods are a special kind of function that are defined within a class.
The argument to these functions is the word obj, which is a reference to objects that are made based on this class. 
To reference instances (or objects) of the class, obj will always be the first parameter, 
but it need not be the only one.

The Constructor Method (__init__)
Is used to initialize data. It is run as soon as an object of a class is instantiated. 
The constructor method is automatically initialized. 
You should use this method to carry out any initializing you would like to do with your class objects.

Variables
https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3
Variables are referred to as class variables, whereas variables at the instance level are called instance variables.
When we expect variables are going to be consistent across instances we can define that variable at the class level. 
When we anticipate the variables will change significantly across instances, we can define them at the instance level.

Inheritance
https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
When one subclass can leverage code from another base class.
Classes called child classes or subclasses inherit methods and variables from parent classes or base classes.

Parent Classes (super class)
Parent classes allow us to create child classes through inheritance without having to 
write the same code over again each time.

Child Classes
Child or subclasses are classes that will inherit from the parent class. 
That means that each child class will be able to make use of the methods and variables of the parent class.

Overriding Parent Methods
When we change parent class methods we override them and modify the behaviour in the child class.

The super() Function
With the super() function, you can gain access to inherited methods that have been overwritten in a class object.
Allows call a parent method into a child method to make use of it. 
The super() function is most commonly used within the __init__() method to complete initialization from the parent.

Multiple Inheritance
Multiple inheritance is when a class can inherit attributes and methods from more than one parent class.
Python scans inheritance as you define in the class declaration from bottom to top and from left to right.
If the same method is defined in multiple parent methods, the child class will use the method of the 
first parent declared in its tuple list.

"""

student_objects = [
    PCAP_OOP.Student('john', 'wayne',  'A', 15),
    PCAP_OOP.Student('jane', 'robinson',  'B', 12),
    PCAP_OOP.Student('dave', 'davidson',  'B', 10),
]

print('Printing students:')
for s in student_objects:
    print('---')
    print('\t', s)
    p = super(type(s), s)
    print('\t', p.__str__())
    print('\t', 'Student fullname:', s.fullname)
    print('\t', 'pPerson fullname: ', p.fullname)
