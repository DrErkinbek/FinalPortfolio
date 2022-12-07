"""
Erkinbek
11/15/2022
Write a Python function to multiply all the numbers in a list. The function should
take a list of numbers as a parameter and return the final result of the multiplication.
"""
def multiply_list(my_list):
  new_list = []
  for x in my_list:
    new_list.append(x * x)
  return new_list

print(multiply_list([1, 2, 3, 4, 5]))

list = [1, 3, 4, 5, 6, 7,8]