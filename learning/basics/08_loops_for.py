# START LAB DEFINITION
# Explore loops.
# Practice for with break an continue
# END LAB DEFINITION

#
# https://docs.python.org/3/tutorial/controlflow.html#for-statements
# https://docs.python.org/3/tutorial/controlflow.html#the-range-function
#
line = "-" * 80

# for using a variable to set a range
print(line, "| 01 Range", line, sep="\n")
max = 4
for i in range(max):
    print(i)

# for usig a magical number to set a range and continue instruction
print(line, "| 02 Range and Modulo", line, sep="\n")
for i in range(8):
    if i % 2 == 0:
        continue
    print(i)

# for using magical number to sea a range and break instruction
print(line, "| 03 Break", line, sep="\n")
for i in range(20):
    if i  == 3:
        break
    print(i)


# for to iterate an string
print(line, "| 05 Lower", line, sep="\n")
message="hello WORLD"
for i in message:
    print(i.lower())

print(line)