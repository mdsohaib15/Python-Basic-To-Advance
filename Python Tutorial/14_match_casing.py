x = int(input("Enter the value of x: "))
match x:
   case 0: # if x is 0
     print("x is 0")
   case 4: # if x is 4
     print("x is 4")

   case _  if x == 90:
     print(x ," is 90")
   case _  if x !=90:
      print(x , "is not 90")
   case _:
    print(x)

