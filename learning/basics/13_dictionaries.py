#
# Is a collection that is ordered, changeable, and does not allow duplicates.
# Dictionaries are used to store data values in key-value pairs.
#
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#

countries = [
    {
    "name": "Peru",
    "continent": "America"
    },
    {
    "name": "Spain",
    "continent": "Europe"
    },
    {
    "name": "UK",
    "continent": "Europe"
    },
]

person = {
    "name" : "Jonny",
    "age" : 22,
    "age" : 33,
    "Surname" : "Any"
}

line = "-" * 80

# printing a list's values
print(line, "| 01", line, sep="\n")
print(countries)
print(countries[2])
print(countries[2]["name"])

# printing a list of objects
print(line, "| 02", line, sep="\n")
print(countries)

# iterating a list and accesing an element by name
print(line, "| 03", line, sep="\n")
for country in countries:
    print(country["name"])

# A dictionary store only the last value for a repeated key
print(line, "| 04 duplicates in dictionaries", line, sep="\n")
print("Person : ", person)

# printing keys, values, items
print(line, "| 05", line, sep="\n")
print("Keys   : ", person.keys())
print("Values : ", person.values())
print("Items  : ", person.items())

# pop items
print(line, "| 06", line, sep="\n")
print("Pop    : ", person.popitem())
print("Person : ", person)

# clear items
print(line, "| 07", line, sep="\n")
person.clear()
print("Person : ", person)

# update items
print(line, "| 07", line, sep="\n")
person.update({"year": 2000})
person.update({"year": 2020, "Name": "Jonny"})
print("Person : ", person)