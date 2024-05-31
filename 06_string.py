name = "sohaib"
print("Hello, " + name)
print('He said, "I want to eat an apple".')

# # Three types of strings

a = "Sohaib"
a = '''Sohaib'''
a = 'Sohaib'

a = "sohaib's"      # --> Use this if you has a single quote in your line 
b = 'sohaib"s'      # --> Use this if you has a double quote in your line
c = '''sohaib's'''  # --> Use this if you has a trple quote in your line
print(a)
print(b)
print(c)

apple = '''He said,
Hi,  
I am Good 
I want to eat an apple'''
print(apple)
print("Lets use a for loop\n")
for character in name:
  print(character)
for character in apple:
  print(character)