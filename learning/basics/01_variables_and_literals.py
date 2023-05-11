# START LAB DEFINITION
# Explore different type of variable definitions
# Practice numeric variables
# Practice string variables
# Practice boolean variables
# Practice assign multiple values to multiple variables in a single line
# END LAB DEFINITION

# Numbers
integer = 100
octal = 0o123
hexadecimal = 0x123
floating = 100.123

print(integer, octal, hexadecimal, floating, sep="\n")
repetitions = 80
print("-" * repetitions)


# Strings
double_quotes = "String using double quotes"
single_quotes = 'String using single quotes'
using_single_quotes = "String using 'single quotes'"
using_double_quotes = 'String using "double quotes"'
escaping_single_quotes = 'String escaping \'single quotes\' '
escaping_double_quotes = "String escaping \"double quotes\" "

print(double_quotes, single_quotes, using_single_quotes, using_double_quotes, escaping_single_quotes, escaping_double_quotes, sep="\n")
print("-" * repetitions)


# Boolean
true_value = True
false_value = False
true_value_numeric = 1
false_value_numeric = 0

print(true_value, false_value, true_value_numeric, false_value_numeric, sep="\n")
print("-" * repetitions)


# Assigning multiple values to multiple variables in a single line
x,y = (5.0, 10)
print(x, y, sep=" - ")

x,y = ("hello", 10)
print(x, y, sep=" - ")

x,y = (5.0, True)
print(x, y, sep=" - ")

print("-" * repetitions)