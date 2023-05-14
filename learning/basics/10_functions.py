
# Docstrings conventions:  https://peps.python.org/pep-0257/ 

line = "-" * 80

def ask_number():
    str = input("introduce a number: ")
    return int(str)

def ask_number_v2():
    """This function does same as ask_number but simplified in one single line.
    This function has no parametes.
    """
    return int(input("introduce a number: "))

def add_numbers(x, y):
    """This function perform addition for two numbers.

    Keyword arguments:

    x -- integer value (without default value)
    y -- integer value (without default value)
    """
    return x + y;

def divide_numbers(x=0, y=0):
    """This function perform division for two numbers.

    Keyword arguments:

    x -- integer value (default 0), should be greater than y.
    y -- integer value (default 0)
    """
    return x / y;

def print_result(num):
    """This method print the result"""
    print("The result is: ", num) 

def is_even(num):
    """This funtion returns None or True depending on the value of num"""
    if(num % 2 == 0):
        return True

#
# Like java, parameters are passed by value for primitives (int,string) and by reference in case of lists
#

print(line, "01 Addition", line, sep="\n")

ix = ask_number()
iy = ask_number_v2()
res = add_numbers(ix, iy)
print_result(res) 
print("Is even:", is_even(res))

print(line, "02 Division", line, sep="\n")

print_result( divide_numbers(ix, iy))     # parameter position matter
print_result( divide_numbers(y=iy, x=ix)) # you can pass parameters using the variable name, parameter posistion does not matter


# variable scopes
print(line, "03 Variable scopes", line, sep="\n")

num = 100
global_num = 200
def print_num():
    num = 50          # shadows the global num value
    global local_num  # makes a local variable definition global
    local_num = 25
    print("Num value inside the method is:", num)
    print("Global num value inside the method is:", global_num)
    print("Local num value inside the method is:", local_num)

print_num()
print("Num value outside the method is:", num)
print("Global num value outside the method is:", global_num)
print("Local num value outside the method is:", local_num)


# Dinamic parameter number
print(line, "04 Dynamic parameter number", line, sep="\n")

def my_function(*students):
  print("The tallest student is " + students[2])

my_function("James", "Ella", "Jackson")


# Inner function
print(line, "05 Inner function", line, sep="\n")

def my_function():
  x = 20
  def my_inner_function():
    print(x)
  my_inner_function()
my_function()


# Tuple
print(line, "05 Tuple", line, sep="\n")

def my_function(*argv):
  print(argv)

my_function('Hello', 'World!')

print(line)