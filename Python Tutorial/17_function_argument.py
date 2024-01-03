print("Default Argument:")
## Default Arguments:(It can give one value & second value will be taken from the default arguent)
def avg(a=2,b=6):
    print("The average is :",(a+b)/2)
avg()
avg(2,4) ##--> we can provide value later
avg(3) ##--> we can also provide only one value and other value is given by default
avg(b=3) ##--> we can also provide only one value and other value is given by default

## Example 1:
def name(firname="Leon",midname="S",lastname="keneddy"):
    print("Hello!",firname,midname,lastname)
name()
name("Claire") #--> first default name is replaced by Claire 
name(midname="Ethan") #--> second default name is replaced by ethan

print("Keyword Argument:")
## Keyword Argumnet:(You can order of arguments)
def avg(a=12,b=8):
    print("The AVG of a and b is:",(a+b)/2)
avg()

print("Required Arguments:")
## Required Arguments:(Argument which are mendatory to provide)
def avg(a ,b, c=3): #-> in this case a & b is required arguments
    print("The avg of a,b & c is :",(a+b+c)/3)
avg(a=6,b=9)

print(("Variable Length Argument:"))
# Variable Length Argument:
# by using tuple method 
print("Key Arbitory Argument:")
# Key Arbitory Argument
# by using dic method
print("Return Statement:")
# Return Statement:(It store in variable Return means take this value and go back)
def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
c=avg(5,6,7)
print(c)