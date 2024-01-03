# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeablle meaning we can not alter them after creation.

tuple1 = (1,2,3,4,5,6)
print(tuple1)
print(type(tuple1))

# Accessing tuple items:
# 1. Positive Indexing:
country = ("Spain", "Japan", "Pakistan")
print(country[0])
print(country[1])
print(country[2])

# 2.Negative Indexing:
country = ("Newzealand", "Pakistan", "Japan", "India", "Iran")
print(country[-1])
print(country[-2])
print(country[-3])
print(country[-4])
print(country[-5])

# 3. Check for item:(by using 'in' keywords)
country = ("Newzealand", "Pakistan", "Japan", "India", "Iran")
if "Japan" in country:
  print("Japan is present")
else:
  print("Japan is absent")

# 4. Range of Index:
animals = ("cat", "monkey", "dog", "bat", "mouse", "cow", "goat","horse", "donkey")
print(animals[1:4]) ## using poitive indexes
print(animals[-7:-2]) ## using negativve indexes