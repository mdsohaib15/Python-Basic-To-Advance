print("----------------------Arithmetic Operators------------------------------")
a = 10
b = 4 
print("The value of 10+4 is", 10+4)  # ~> Addition
print("The value of 10-4 is", 10-4)  # ~> Substraction
print("The value of 10*4 is", 10*4)  # ~> Multiplication 
print("The value of 10/4 is", 10/4)  # ~> Division
print("The value of 10//4 is",10//4) # ~> Floor Division  --> remove '.' value
print("The value of 10**4 is",10**4) # ~> Exponential 
print("The value of 10%4 is", 10%4)  # ~> Modulus  --> give remainder

print("-----------------------Assignment Operator------------------------------") 
a = b = c = d = 34
a += 12 #--> equal to a = a+12
b -= 12 #--> equal to b = b-12
c *= 12 #--> equal to c = c*12
d /= 12 #--> equal to d = d/12
print(a) 
print(b)
print(c) 
print(d) 

print("----------------------Comparison Operator-------------------------------")
a = (12>7)
b = (12<7)
c = (12>=7)
d = (12<=7)
e = (12==7)
f = (12!=7)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("-----------------------Logical Operator---------------------------------")
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or bool2) )
print("The value of not bool2 is", not bool2)
# and | Returns True if both statements are true	                    |x < 5 and  x < 10   |
# or  |	Returns True if one of the statements is true     	|x < 5 or x < 4	 |
# not | Reverse the result, returns False if the result is true	not |x < 5 and x < 10|

print("----------------------Bitwise operator---------------------")
x = 5
y = 2
# bin() convert to binary
z = bin(12)
print(z)
print(8>>2) # signed right shift
print(2<<8) # zero fill left shift 

print("----------------------Identity operator---------------------")
print("----------------------Membership operator---------------------")