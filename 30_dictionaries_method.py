# Dictionary Methods
# Dictionary uses several built-in methods for manipulation.They are listed below

# 1-update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
print("\n1-update()")
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)

# 2-clear():
# The clear() method removes all the items from the list.
print("\n2-clear():")
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

# 3-pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.
print("\n3-pop():")
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('age')
print(info)

# 4-popitem():
# The popitem() method removes the last key-value pair from the dictionary.
print("\n4-popitem():")
info = {'name':'Karan', 'age':19, 'eligible':True}
info.popitem()
print(info)

# 5-del:
# we can also use the del keyword to remove a dictionary item.
print("\n5-del:")
info = {'name':'Karan', 'age':19, 'eligible':True}
del info
# print(info) # shows an erroe
info = {'name':'Karan', 'age':19, 'eligible':True}
del info['age']
print(info)

empty = {}
print("\nThe output of empty is ",empty)