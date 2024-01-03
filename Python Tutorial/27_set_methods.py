# 1-isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
print("\n1-isdisjoint():")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
cities3 = cities1.isdisjoint(cities2)
print(cities3) #--> print False

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Dubai", "Texas", "Seoul", "Kabul"}
cities3 = cities1.isdisjoint(cities2)
print(cities3) #--> print True

# 2-issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
print("\n2-issuperset():")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
cities3 = cities1.issuperset(cities2)
print(cities3) #--> print False

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities1.issuperset(cities2)) #--> print True

# 3-issubset():
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
print("\n3-issubset():")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities1)) #--> print True

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 ={"Kabul", "Texas"}
print(cities2.issubset(cities1)) #--> print False

# 4-add()
# If you want to add a single item to the set use the add() method.
print("\n4-add()")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Texas")
print(cities)

# 5-update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
print("\n5-update()")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities1.update(cities2)
print(cities1)

# 6-remove()/discard()
# We can use remove() and discard() methods to remove items form list.
print("\n6-remove()/discard()")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
# cities.remove("Tokyo1") => gives an error
print(cities)
cities.discard("Tokyo1") #-> not raise an error
cities.discard("Tokyo") 
print(cities)
# Note: if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

# 7-pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
print("\n7-pop()")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# 8-del
# del is not a method, rather it is a keyword which deletes the set entirely.
print("\n8-del")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities

# 9-clear():
# This method clears all items in the set and prints an empty set.
print("\n9-clear():")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if item exists
# You can also check if an item exists in the set or not.
print("\nCheck if item exists")
info = {"Ashley", 20, True, 4.8}
if "Ashley" in info:
  print("Ashley is present")
else:
  print("Ashley is Absent")