# Docstrings in python:
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)

def multiplier(a, b):
    """Takes in two numbers, returns their product."""
    print(a*b)
multiplier(5,2)
print(multiplier.__doc__)

