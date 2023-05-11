# START LAB DEFINITION
# Explore loops.
# Practice for with break an continue
# END LAB DEFINITION
repetitions = 20

# for using a variable to set a range
print("--01--" * repetitions)
max = 4
for i in range(max):
    print(i)

# for usig a magical number to set a range and continue instruction
print("--02--" * repetitions)
for i in range(8):
    if i % 2 == 0:
        continue
    print(i)

# for using magical number to sea a range and break instruction
print("--03--" * repetitions)
for i in range(20):
    if i  == 3:
        break
    print(i)


# for to iterate an string
print("--04--" * repetitions)
message="hello WORLD"
for i in message:
    print(i.lower())

print("-" * (repetitions * 6))