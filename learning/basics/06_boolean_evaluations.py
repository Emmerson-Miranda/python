# START LAB DEFINITION
# Explore boolean evaluations when we use it conditions using variables and in-fly values.
# Practice and
# Practice or
# Practice not
# END LAB DEFINITION

repetitions = 80

# AND (evaluation can be on the fly)
print("-" * repetitions)

a,b=True,True
print("(1) and evaluation", a and b)

a,b=True,False
print("(2) and evaluation", a and b)

a,b=False,True
print("(3) and evaluation", a and b)

a,b=False,False
print("(4) and evaluation", a and b)

# OR (evaluation can be assigned to a variable)
print("-" * repetitions)

a,b=True,True
condition = a or b
print("(5) or evaluation", condition)

a,b=True,False
condition = a or b
print("(6) or evaluation", condition)

a,b=False,True
condition = a or b
print("(7) or evaluation", condition)

a,b=False,False
condition = a or b
print("(8) or evaluation", condition)

# NOT 
print("-" * repetitions)
a,b=True,False

condition = not a
print("(9) not evaluation", condition)

condition = not b
print("(10) not evaluation", condition)

# Multiple conditions 
print("-" * repetitions)

evaluation = (True or False) and (True and True)
print("(13) evaluation", evaluation)

evaluation = (True and False) and (True and True)
print("(14) evaluation", evaluation)

evaluation = (True and False) or (True and True)
print("(15) evaluation", evaluation)

evaluation = (True and False) and (False and True)
print("(16) evaluation", evaluation)

evaluation = (True and True) and (True and True)
print("(17) evaluation", evaluation)

evaluation = (True and True) and not (True and True)
print("(17) evaluation", evaluation)

evaluation = not (True and True) and not (True and True)
print("(18) evaluation", evaluation)

evaluation = (not evaluation)
print("(19) evaluation", evaluation)