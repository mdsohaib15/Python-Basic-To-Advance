# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.


s = {2, 3, 4, 2}
print(s)

# python doesn't give us maintained order in list
info = {"Leon", 26, 5.11, True, 26}
print(info)

# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set.
empty = {}  #--> class 'dict'
print(type(empty)) 
empty = set()
print(type(empty))
for value in info:
  print(value)