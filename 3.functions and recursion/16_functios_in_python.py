def calculateaverage(a, b):
    avg = (a+b)/2
    print(avg)

## Example 1:
## by using function:
a = 2
b = 8
print("The average of a & b by using fuction is:")
calculateaverage(a, b)

## without using function:
a = 2
b = 8
avg = (a+b)/2
print("The average of a & b is:\n",avg)

## Example 2:
## by using function:
c = 6
d = 10
print("The average of c & d is:")
calculateaverage(c,d)

## without function:
c = 6
d = 10
avg = (c+d)/2
print("The average of c & d is:\n",avg)

## Example 3:
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
    
## using fuction:
a = input("Enter first number:")
b = input("Enter second number:")
isGreater(a,b)

# not using fuction:
a = input("Enter first number:")
b = input("Enter second number:")
if(a>b):
    print("First number is greater ")
else:
    print("Secong number is greater or equal")

## pass:
def islesser(a,b):
    pass ## Donot show error by using "pass" function
