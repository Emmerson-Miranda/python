import inspect

repetitions = 80
line = "-" * repetitions

def enumerate_list():
  """ Iterate a list and get the index at same time """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  list1 = [5, 6, 7, 8]
  print("Source : ", list1)
  for i, j in enumerate(list1):
      print(i, j)
  
enumerate_list()

def replace_subset():
  """ Replace a subset inside a list """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  list1 = [0, 3, 4, 1, 2, 5 , 15, 25]
  print("Before : ", list1)
  list1[2:5]=[8,9] # replaces the subset between 2:5 with a new values 8,9
  print("After : ", list1)

replace_subset()

def select_countries():
  """ Inline for to select a contry given a condition in an if """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  countries = [['Egypt', 'USA', 'India'],['Peru', 'Mexico', 'Spain'], ['Norway', 'England', 'France']]
  print("Source : ", countries)
  
  countries2 = [country for sublist in countries for country in sublist]
  countries3 = [country for sublist in countries for country in sublist if len(country) < 6]
  countries4 = [country for sublist in countries for country in sublist if len(country) >= 6]
  countries5 = [country for sublist in countries for country in sublist if country.startswith("E") ]
  countries6 = [sublist for sublist in countries for country in sublist if country.startswith("E") ]

  print("Output 2: ", countries2)
  print("Output 3: ", countries3)
  print("Output 4: ", countries4)
  print("Output 5: ", countries5)
  print("Output 6: ", countries6)

select_countries()

def generate_list():
  """ Generate a list and print elements """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  list = [j for j in range(10)] 
  print("Source : ", list)
  print("Elements : ", list[4:6])

generate_list()

def generate_2d_matrix():
  """ Generate a 2D matrix and print some elements """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  matrix = [[j for j in range(5)] for i in range(3)] 
  print("2D matrix : ", matrix)
  print("Element   : ", matrix[2][1])

  matrix2 = [[j+i for j in range(5)] for i in range(3)] 
  print("2D matrix : " , matrix2)
  submatrix = [sublist for sublist in matrix2 for element in sublist if element == 5]
  print("Submatrix : ", submatrix)
  print("Element   : ", matrix2[2][1])

generate_2d_matrix()

def generate_3d_matrix():
  """ Generate a 3D matrix and print some elements """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  matrix = [[[k+j+i for k in range(3)] for j in range(3)] for i in range(3)]
  print("3D matrix : ", matrix)
  print("Element   : ", matrix[2][1])

generate_3d_matrix()


def filter_odd_numbers():
  """ Filter odd numbers and use nested function """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")
 
  def get_odd_func(numbers):
      odd_numbers = [num for num in numbers if num % 2]
      return odd_numbers
  
  def get_mod3_func(numbers):
      numbers = [num for num in numbers if num % 3]
      return numbers
  
  def get_not_odd_func(numbers):
      not_odd_numbers = [num for num in numbers if not(num % 2)]
      return not_odd_numbers

  list1 = [i for i in range(14)]
  print("Source : " ,  list)
  print("Output mod 2     : ", get_odd_func(list1))
  print("Output not mod 2 : ", get_not_odd_func(list1))
  print("Output not mod 2 : ", list(filter(lambda x: x % 2 == 0, list1)))
  print("Output mod 3     : ", get_mod3_func(list1))

filter_odd_numbers()

def multiply_lists():
  """ Multiply lists and use nested function """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  def mult_list(times, numbers):
    return times * numbers

  numbers = [1, 2, 3]
  print("Source : ", numbers)
  print("2 times: ", mult_list(2, numbers)) 
  print("3 times: ", mult_list(3, numbers)) 

multiply_lists()


def sum_min_max():
  """ Other operation for lists """
  print(line, "\n", inspect.currentframe().f_code.co_name, "\n", line, sep="")

  list = [5, 6, 7, 8, 3]
  print("Source : ", list)
  print("sum : ", sum(list))
  print("min : ", min(list))
  print("max : ", max(list))

sum_min_max()

print("-" * 100)





