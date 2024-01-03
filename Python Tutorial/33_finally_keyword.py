# Finally Clause:
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred :(")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)

# Example:-
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")



def fun1():
  try:
    i = float(input("Enter a decimal number: "))
    print(i)
    return 1
  except:
    print("Number is not a decimal number!")
    return 0 
  finally:
    print("LOL!")

q = fun1()
print(q)