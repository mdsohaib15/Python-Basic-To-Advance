# *******Readline() The readline() method returns one line from the file item.
# f=open('marks.txt','r')
# print(f.readline())
# f.close()
# f = open("newfile2.txt","r")
# while True:
#           line = f.readline()
#           if not line:
#                     print(line,type(line))
#                     break
#           print(line)
# f.close()

#Example:
# f = open('marks.txt','r')
# i=0
# while True:
#           i+=1
#           line = f.readline()
#           if not line:
#                     break
#           m1 = line.split(',')[0] #-> these 3 m data are stored in form of strings when we want int we typecasting it 
#           m2 = line.split(',')[1]
#           m3 = line.split(',')[2]
#           print(f'Marks of student {i} in maths is {m1}')
#           print(f'Marks of student {i} in science is {m2}')
#           print(f'Marks of student {i} in computer is {m3}')
          

# ****writelines*******
# The writelines() method writes the items of a list to the file.
# f=open('line.txt','w')
# lines=['line1\n','line2\n','line3']
# f.writelines(lines)
# f.close()

# ******* readlines********
# The readlines() method returns a list containing each line in the file as a list item.
f=open('marks.txt','r')
print(f.readlines())
f.close()