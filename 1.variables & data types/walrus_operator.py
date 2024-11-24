# **********WALRUS OPERATOR***********
# assign values to variables as part of a larger expression
# thrown an error
# a=True
# print(a=False)

a=True
print(a:=False)

# without walrus operator:
# example
fruits = list() # make empty list
while True:
          fruit=input('what fruit do you like?')
          if fruit =="quit":
                    break
          fruits.append(fruit)
print(fruits)

# with walrus operator:
# example
foods = list()
while (food := input('what food do you like?')) != 'quit':
          foods.append(food)
print(foods)
