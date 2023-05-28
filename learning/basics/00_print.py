# START LAB DEFINITION
# Explore print built-in method
# Practice support for multiple parameters
# Practice support to customize separators
# Practice write to a text file
# END LAB DEFINITION

# https://www.w3schools.com/python/ref_func_print.asp
#

# 1 - simple
print("Hello world")

# 2 - multiple parametes
print("This", "is", "a", "hello", "world")
# 3 - custom parameter separator 
print("This", "is", "a", "hello", "world", sep="-")

# 4 - custom parameter separator and end of line
print("This", "is", "a", "hello", "world", sep="_", end="@")

# 5 - sending output to a file
with open('00_print.txt', 'w') as f:
    print("1", "This", "is", "a", "hello", "world", sep="=", end="\n", file=f)
    print("2", "This", "is", "a", "hello", "world", sep="=", end="\n", file=f)

print("")

# force print to flush information https://realpython.com/python-flush-print-output/
import functools

print = functools.partial(print, flush=True) # overriding print signature to add flush parameter
print('This is an example forcing print to flush memory.')