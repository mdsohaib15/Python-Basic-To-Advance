# **** seek*********
# In Python, seek() function is used to change the position of the File Handle to a given specific position. 
# ***********88tell*********
# Python tell function is used to determine the current position or location of the file pointer. 
f = open('seek.txt','r')

# sets Reference point to tenth 
# index position from the beginning
f.seek(10)
data = f.read(46) # -> 46 denote where the line prints

print(data)
# prints current position
print(f.tell())

f.close()

# ********trancate************
# truncate() file method allows the user to resize the file to a given number of bytes when the file is accessed through the append mode.
with open('truncate.txt','w') as f:
          f.write('Hello World')
          f.truncate(5)
with open('truncate.txt','r') as f:
          print(f.read())