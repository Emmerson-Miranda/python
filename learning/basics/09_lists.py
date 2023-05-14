
# a list is a collection of primitive values or objects
letters = ["a","b","c","d","e"]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10]
]

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

line = "-" * 80

# printing a list's values
print(line, "| 01", line, sep="\n")

print(letters)
print(matrix)
print(countries)


# list's lenght
print(line, "| 02", line, sep="\n")
size = len(letters)
print("letters list size:", size)

# deleting an object from a given position
print(line, "| 03", line, sep="\n")
del letters[2]
print(letters)

# inserting an element
print(line, "| 04", line, sep="\n")
letters.insert(2, "CCC")
print(letters)

# accessing and printing an specific element
print(line, "| 05", line, sep="\n")
print(letters[3])
print(countries[2])
print(countries[2]["name"])

# extracting a subset of elements (slicing)
print(line, "| 06", line, sep="\n")
print(letters[2:4])
print(letters[:3])
print(letters[2:])
print(letters[1:-1])
print(letters[:])
print(letters[::-1]) # reverse
print(letters)
print( letters[::2]) # return elements jumping two
print(letters[::1]) # full list
print(letters[::3]) # extract position 0 and 3 from the list
print(letters.pop(2)) # extract and remove the index 2
print(min(letters)) 


# appending an element to the end of the list
print(line, "| 07", line, sep="\n")
letters.append("FFF")
print(letters)

# accessing to the last element of the list
print(line, "| 08", line, sep="\n")
print(letters[-1])

# sorting elements
print(line, "| 09", line, sep="\n")
letters.sort()
print(letters)

# reversing the sort
print(line, "| 10", line, sep="\n")
letters.reverse()
print(letters)

# printing a list of objects
print(line, "| 11", line, sep="\n")
print(countries)

# iterating a list and accesing an element by name
print(line, "| 12", line, sep="\n")
for country in countries:
    print(country["name"])

# searching
print(line, "| 13", line, sep="\n")
print("CCC" in letters)
print("ABC" in letters)
print("ABC" not in letters)

# lists are pointers to the memory position
print(line, "| 14", line, sep="\n")

letters = ["a","b","c","d","e"]
letters2 = letters      # letters2 will reference to same info as letters
letters3 = letters[:]   # letters3 is a copy in different memory location

letters.append("GGG")
letters2.append("HHH")
letters3.append("III")

print(letters)
print(letters2)
print(letters3)

print(line)

