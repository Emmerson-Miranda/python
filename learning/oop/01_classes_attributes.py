
class MyClass01:
    pass #https://www.w3schools.com/python/ref_keyword_pass.asp


class MyClass02:
    text = 'Hello World'


class MyClass03:
    text = 'Hello World'
    __counter = 0

    def __init__(self, year=1821, month='July', day=28, country='Peru'):
        print("Instantiating object of", self.__class__.__name__, "counter", self.__class__.__counter)
        MyClass03.__counter += 1
        self.year = year
        self.month = month
        self.day = day
        self.__country = country

    def __del__(self):
        print("Destroying object of", self.__class__.__name__, "counter", self.__class__.__counter)
        self.__class__.__counter -= 1


line = "-" * 80

print(line, "| 01 __dic__", line, sep="\n")
my_obj = MyClass01()
print(my_obj.__class__.__name__, "Instance __dic__", type(my_obj.__dict__), my_obj.__dict__)
print(my_obj.__class__.__name__, "Class __dic__   ", type(MyClass01.__dict__), MyClass01.__dict__)
print(my_obj.__class__.__name__, "Class __dic__   ", type(my_obj.__class__.__dict__), my_obj.__class__.__dict__)

print(line, "| 02 __dic__ class attribute 'text'", line, sep="\n")
my_obj = MyClass02()
print(my_obj.__class__.__name__, "Instance __dic__", type(my_obj.__dict__), my_obj.__dict__)
print(my_obj.__class__.__name__, "Class    __dic__", type(my_obj.__class__.__dict__), my_obj.__class__.__dict__)

print(line, "| 03 adding properties to object on-the-fly", line, sep="\n")
my_obj.myatt1 = 5
my_obj.myatt2 = "new instance attribute"
MyClass02.another_att = "new class attr"
print(my_obj.__class__.__name__, "Instance __dic__", type(my_obj.__dict__), my_obj.__dict__)
print(my_obj.__class__.__name__, "Class __dic__   ", type(my_obj.__class__.__dict__), my_obj.__class__.__dict__)

print(line, "| 04 has attribute", line, sep="\n")
print(my_obj.__class__.__name__, "instance hasattr myatt1     :", hasattr(my_obj, "myatt1"))
print(my_obj.__class__.__name__, "instance hasattr myatt2     :", hasattr(my_obj, "myatt2"))
print(my_obj.__class__.__name__, "instance hasattr myatt3     :", hasattr(my_obj, "myatt3"))
print(my_obj.__class__.__name__, "class hast attr text        :", hasattr(MyClass02, "text"))
print(my_obj.__class__.__name__, "class hast attr another_att :", hasattr(MyClass02, "another_att"))
print(my_obj.__class__.__name__, "class hast attr unknown_att :", hasattr(MyClass02, "unknown_att"))
print(MyClass03.__name__, "class hast attr counter     :", hasattr(MyClass03, "__counter"))
print(MyClass03.__name__, "class hast attr counter     :", hasattr(MyClass03, "_MyClass03__counter"))

print(line, "| 05 printing class attributes", line, sep="\n")
print("MyClass02.text        : ", MyClass02.text)
print("MyClass02.another_att : ", my_obj.__class__.another_att)

my_obj = MyClass03()
my_ob2 = MyClass03(1823, 'Julio', 20, 'Colombia')
my_ob2.__anotherprop = 'new private prop'
print(my_obj.__class__.__name__, " class properties :", my_obj.__class__.__dict__)
print(my_ob2.__class__.__name__, " class properties :", my_ob2.__class__.__dict__)
print(my_obj.__class__.__name__, " my_obj properties:", my_obj.__dict__)
print(my_ob2.__class__.__name__, " my_ob2 properties:", my_ob2.__dict__)

print(line, "| 06 printing instance attributes", line, sep="\n")
print("Att added to the instance dynamically      :", my_ob2.__anotherprop)
print("Att added to the instance from constructor :", my_ob2.day)
print("Accessing hidden Att at instance level     :", my_ob2._MyClass03__country)
print("Accessing hidden Att at instance dictionary:", my_ob2.__dict__['_MyClass03__country'])

print(line, "| 07 deleting objects", line, sep="\n")
del my_ob2
print(my_obj.__class__.__name__, " class properties :", my_obj.__class__.__dict__)
print("Counter value from hidden att: ", MyClass03._MyClass03__counter)
print("Counter value from class dict : ", MyClass03.__dict__['_MyClass03__counter'])
print(line, "| END", line, sep="\n")
