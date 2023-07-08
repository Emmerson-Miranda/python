"""
PCAP-31-03 4.4 – Discover the class structure

    introspection and the hasattr() function (objects vs classes)
    properties: __name__, __module__ , __bases__

"""
import PCAP_OOP

"""
https://docs.python.org/3/reference/datamodel.html
https://docs.python.org/3/library/inspect.html

__name__
The function’s name.
The class name.

__module__
The name of the module the function was defined in, or None if unavailable.
The name of the module in which the class was defined.

__bases__
A tuple containing the base classes of the class object, in the order of their occurrence in the base class list.

hasattr(object, name)
The arguments are an object and a string. 
The result is True if the string is the name of one of the object’s attributes, False if not.
    
"""
john = PCAP_OOP.Student('john', 'wayne',  'A', 15)
print('john.info()      :', john.info())

print('john.__module__  :', john.__module__)
print('john.__class__   :', john.__class__)
print('type(john)       :', type(john) )
print('type(PCAP_OOP.Student)      :', type(PCAP_OOP.Student) )

print('PCAP_OOP.Student.__module__ :', PCAP_OOP.Student.__module__)

print('PCAP_OOP.Person.__bases__   :', PCAP_OOP.Person.__bases__)
print('PCAP_OOP.Student.__bases__  :', PCAP_OOP.Student.__bases__)

print('isinstance(john, PCAP_OOP.Student) :', isinstance(john, PCAP_OOP.Student))
print('isinstance(john, PCAP_OOP.Person)  :', isinstance(john, PCAP_OOP.Person))

print("hasattr(john, '__init__')   :", hasattr(john, '__init__'))
print("hasattr(john, 'fullname')   :", hasattr(john, 'fullname'))
print("hasattr(john, 'name')       :", hasattr(john, 'name'))
print("hasattr(john, 'middlename') :", hasattr(john, 'middlename'))

print("hasattr(PCAP_OOP.Student, 'anything')          :", hasattr(PCAP_OOP.Student, 'anything'))
print("hasattr(PCAP_OOP.Student, '_Student__counter') :", hasattr(PCAP_OOP.Student, '_Student__counter'))
