# START LAB DEFINITION
# Explore different type of variable definitions
# Practice numeric variables
# Practice string variables
# Practice boolean variables
# Practice assign multiple values to multiple variables in a single line
# END LAB DEFINITION

line = "-" * 80


# Numbers
print(line, "| 01 Numbers", line, sep="\n")

integer = 100
octal = 0o123
hexadecimal = 0x123
floating = 100.123

print(integer, octal, hexadecimal, floating, sep="\n")


# Strings
print(line, "| 02 Strings", line, sep="\n")
double_quotes = "String using double quotes"
single_quotes = 'String using single quotes'
using_single_quotes = "String using 'single quotes'"
using_double_quotes = 'String using "double quotes"'
escaping_single_quotes = 'String escaping \'single quotes\' '
escaping_double_quotes = "String escaping \"double quotes\" "

print(double_quotes, single_quotes, using_single_quotes, using_double_quotes, escaping_single_quotes, escaping_double_quotes, sep="\n")


# Boolean
print(line, "| 03 Boolean", line, sep="\n")
true_value = True
false_value = False
true_value_numeric = 1
false_value_numeric = 0

print(true_value, false_value, true_value_numeric, false_value_numeric, sep="\n")


# Assigning multiple values to multiple variables in a single line
print(line, "| 04 Multiple assignment", line, sep="\n")
x,y = (5.0, 10)
print(x, y, sep=" - ")

x,y = ("hello", 10)
print(x, y, sep=" - ")

x,y = (5.0, True)
print(x, y, sep=" - ")

print(line)