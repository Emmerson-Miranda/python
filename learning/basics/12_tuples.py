#
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
#

line = "-" * 80

print(line, "| 01", line, sep="\n")
t = 1, 2, 3
print("Tuple", t)
print("Type", type(t))

print(line, "| 02", line, sep="\n")
t = (1,)
print("Tuple", t)
print("Type", type(t))

print(line, "| 03", line, sep="\n")
def print_parameters(*args):
    print("Tuple", args)
    print("Type", type(args))
print_parameters(1,2,3,4,5)
print_parameters(111)