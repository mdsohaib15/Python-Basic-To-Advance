# list.sort()
# This method sorts the list in ascending order. The original list is updated

num = [4,10,3,6,2,8,9,7,1,5]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.sort(reverse=False)
print(num)

# append():
# This method appends items to the end of the existing list.
colors = ["blue", "red", "voilet"]
colors.append("black")
print(colors)
# reverse()
# This method reverses the order of the list.
num = [3,6,9,12,15,18]
num.reverse()
print(num)

# index()
# This method returns the index of the first occurrence of the list item.
colors = ["red", "blue", "green", "black"]
print(colors.index("green"))

# count()
# Returns the count of the number of items with the given value.
colors = ["red", "blue", "green","red", "black","red"]
print(colors.count("red"))

# copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
colors = ["voilet","green","blue","black"]
colors.insert(1,"red")
print(colors)

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

# Concatenating two lists:
# You can simply concatenate two lists to join two lists.
colors1 = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors1 + colors2)