
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

repetitions = 20

# printing a list's values
print("--01--" * repetitions)

print(letters)
print(matrix)
print(countries)


# list's lenght
print("--02--" * repetitions)
size = len(letters)
print("letters list size:", size)

# deleting an object from a given position
print("--03--" * repetitions)
del letters[2]
print(letters)

# inserting an element
print("--04--" * repetitions)
letters.insert(2, "CCC")
print(letters)

# accessing and printing an specific element
print("--05--" * repetitions)
print(letters[3])
print(countries[2])
print(countries[2]["name"])

# extracting a subset of elements (slicing)
print("--05--" * repetitions)
print(letters[2:4])
print(letters[:3])
print(letters[2:])
print(letters[1:-1])
print(letters[:])

# appending an element to the end of the list
print("--06--" * repetitions)
letters.append("FFF")
print(letters)

# accessing to the last element of the list
print("--07--" * repetitions)
print(letters[-1])

# sorting elements
print("--08--" * repetitions)
letters.sort()
print(letters)

# reversing the sort
print("--09--" * repetitions)
letters.reverse()
print(letters)

# printing a list of objects
print("--10--" * repetitions)
print(countries)

# iterating a list and accesing an element by name
print("--11--" * repetitions)
for country in countries:
    print(country["name"])

# searching
print("--12--" * repetitions)
print("CCC" in letters)
print("ABC" in letters)
print("ABC" not in letters)

# lists are pointers to the memory position
print("--13--" * repetitions)

letters = ["a","b","c","d","e"]
letters2 = letters      # letters2 will reference to same info as letters
letters3 = letters[:]   # letters3 is a copy in different memory location

letters.append("GGG")
letters2.append("HHH")
letters3.append("III")

print(letters)
print(letters2)
print(letters3)

print("-" * (repetitions * 6))