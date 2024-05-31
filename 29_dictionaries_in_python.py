# Python Dictionaries:
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
# dictionary is combonation of key-value pairs:
dic = {
  344 : "Chris",
  244 : "Claire",
  199 : "Jill",
  400 : "Neha"
}
print(dic[244]) # -> syntax (dic-name[key])--> it print the value 
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
# I. Accessing single values:
print("\nI. Accessing single values:")
print(info['name'])
print(info.get('name'))
# print(info['name2']) #->  it shows an error 
print(info.get('name2')) #-> it print None

info = {'name':'Karan', 'age':19, 'eligible':True}
# II. Accessing multiple values:
print("\nII. Accessing multiple values:")
print(info.values())

# III. Accessing keys:
print("\nIII. Accessing keys:")
print(info.keys())


for key  in info.keys():
  print(info[key])

for key in info.keys():
  print(f"The value corresponding to the {key} is {info[key]}")

# IV. Accessing key-value pairs:
print("\n")
print(info.items())

for key,value in info.items():
  print(f"The value corresponding to the {key} is {value}")