## Lists are ordered collection of data items,store multiple item in a single variable,it is changable 
marks = [ 86 , 92 , 23 , 34 , 76 , 67 ]
print(marks)
print(type(marks))

## List Index:
## Positive Indexing:
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

## Negative Indexing:(Convert into positive indexing)
print(marks[-2])
print(marks[len(marks)-2])
print(marks[6-2])
print((marks[4]))
## All have same answer

# a single list can contain items of different data types.
details = ["Leon", 24 , 5.11 , True]
print((details))

## "in" Keyword:
if "Leon" in details:
    print("Yes")
else:
    print("No")
if "24" in details:
    print("YES")
else:
    print("No")
## Same thing apply for strings as well!
if "Leo" in "Leon":
    print("Yes")
else:
    print("No")

## Jump indexing:
marks = [50, 45, 77, 88, 99, 44, 55, 33, 84, 95, 60, 75]
print(len(marks))
print(marks[1:12])
print(marks[1:12:2]) ## Jump indexes:(Printing every 2nd consecutive value withing a given range)
print(marks[1:8])
print(marks[1:8:3])  ## Jump indexes: (Printing every 3rd consecutive value withing a given range)
print("---------------------------------------------------")

## Python will add 0 in the starting & len() in th end:
marks = [50, 45, 77, 88, 99, 44, 55, 33, 84, 95, 60, 75]
print(marks[:])
print(marks[0:len(marks)])

## List Comprehension(Used for creating new list from other iterable list)
list = [i for i in range(5)]
print(list)
list2 = [i for i in range(10) if i%2==0]
print(list2)

# Example 1: Accepts items with the small letter “n” in the new list
names = ["Ethan", "Sarah" , "Claire", "Ashley", "Winters", "Leon", "Kennedy" ]
names_with_n = [item for item in names if "n" in item ]
print(names_with_n)

# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)

names = [ "Leon","Ethan", "Rose", "Sarah" , "Claire", "Ashley", "Jill"]
name_4 = [char for char in names if (len(char)>4)]
print(name_4)