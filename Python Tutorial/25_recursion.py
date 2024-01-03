# Python also accepts function recursion, which means a defined function can call itself.
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) #==> called the factorial(n-1) function inside factorial(n)

print(factorial(5))
# it go inside 'else'.
# It will ne told to calculate 5 * factorial(n==4) so,
# 5 * factorial(4) 
# 5 * 4 * factorial(3) 
# 5 * 4 * 3 * factorial(2) 
# 5 * 4 * 3 * 2 * factorial(1) -> this is n==1 it go inside 'if' & print 1
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
a = int(input("Enter a number:"))
def fibonacci(num):
    if(num==1 or num==0):
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(6))

for i in range(a):
    print(fibonacci(i))

# 0 1 1 2 3 5 8 13....