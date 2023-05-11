# START LAB DEFINITION
# Explore operators
# Practice Add
# Practice Substract
# Practice Multiply
# Practice Divide
# Practice Floor divide
# Practice Modulo
# Practice Exponential
# END LAB DEFINITION

repetitions = 80

# Add
print("-" * repetitions)

x,y = (1, 2)
print("(1)", x + y)

x,y = (1, 3.0)
print("(2)", x + y)

x,y = (1, .4)
print("(3)", x + y)

x,y = (5.0, 1)
print("(4)", x + y)

# Substract
print("-" * repetitions)

x,y = (6, 1)
print("(5)", x - y)

x,y = (6, 2.0)
print("(6)", x - y)

x,y = (6, 0.3)
print("(7)", x - y)

# Multiply
print("-" * repetitions)

x,y = (6, 1)
print("(8)", x * y)

x,y = (6, 2.0)
print("(9)", x * y)

x,y = (6, .5)
print("(10)", x * y)

# Divide
print("-" * repetitions)

x,y = (6, 2)
print("(11)", x / y)

x,y = (6.0, 2.0)
print("(12)", x / y)

x,y = (6.0, .2)
print("(13)", x / y)

# Floor divide
print("-" * repetitions)

x,y = (6, 2)
print("(14)", x // y)

x,y = (6.0, 2.0)
print("(15)", x // y)

x,y = (6.0, .2)
print("(16)", x // y)

# Modulo
print("-" * repetitions)

x,y = (9, 5)
print("(17)", x % y)

x,y = (8.0, 5)
print("(18)", x % y)

# Exponential
print("-" * repetitions)

x,y = (2, 3)
print("(19)", x ** y)

x,y = (5.0, 2)
print("(20)", x ** y)