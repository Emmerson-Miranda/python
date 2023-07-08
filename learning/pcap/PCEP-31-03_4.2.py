"""
PCEP-31-03 4.2 – Employ class and object properties

    instance vs. class variables: declarations and initializations
    the __dict__ property (objects vs. classes)
    private components (instances vs. classes)
    name mangling

"""
import PCAP_OOP

"""

Class Variables
Class variables are defined within the class definition. 
Shared by all instances of the class (have the same value for every instance)
Defined outside of all the methods, typically placed right below the class header and before any method or constructor.
Like java you can access to it also though a class instance.

Instance Variables
For each object or instance of a class, the instance variables values are different.
Unlike class variables, instance variables are defined within methods (i.e. __init__).

name mangling
In name mangling process any identifier with two leading underscore(__identifier) and one trailing underscore 
is textually replaced with _classname__identifier where classname is the name of the current class. 

_single underscore prefix
https://medium.com/analytics-vidhya/python-name-mangling-and-how-to-use-underscores-e67b529f744f
Single leading underscores are used as a weak “internal use” or “private” indicator for methods and data attributes. 
These objects are still totally accessible outside of their parent class at runtime, 
use them as modification of these objects could have unanticipated consequences.
The single-underscore variable naming convention was established in Pep-8.
A common use case where I like to use single underscore variables is on classes where I have some attributes 
which are a calculated value and want to discourage direct modification.
_private objects are not included in 'from x import *' style import statements.

__double__ underscore prefix and postfix
The use of a double-underscore prefix AND postfix are often known as magic or “dunder” methods 
and are meant to be reserved for Python’s internal Type and Class implementation.

"""

john = PCAP_OOP.Student('john', 'wayne',  'A', 15)
print('PCAP_OOP.Student.__dict__ :', PCAP_OOP.Student.__dict__)
print('john.__dict__             :', john.__dict__)
print('dir(john)                 :', dir(john))
print('dir(PCAP_OOP.Student)     :', dir(PCAP_OOP.Student))
