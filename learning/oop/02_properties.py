# Source: https://mathspp.com/blog/pydonts/properties
# A property is an attribute that is computed dynamically

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def name(self):
        return f"{self.first} {self.last}"

    # setter is not mandatory, no presence indicate the property is read-only
    @name.setter
    def name(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @name.deleter
    def name(self):
        self.first = None
        self.last = None


line = "-" * 80

print(line, "| 01 Create person and print name", line, sep="\n")
p1 = Person("John", "Doe")
print("Person : ", p1.name)

print(line, "| 02 Changing last name", line, sep="\n")
p1.last = 'Smith'
print("Person : ", p1.name)

print(line, "| 03 Using property setter", line, sep="\n")
p1.name = 'Marie Curie'
print("Person : ", " first: ", p1.first, " - last: ", p1.last, " - full name: ", p1.name)

print(line, "| 04 delete property", line, sep="\n")
del p1.name
print("Person : ", " first: ", p1.first, " - last: ", p1.last, " - full name: ", p1.name)


print(line, "| END", line, sep="\n")