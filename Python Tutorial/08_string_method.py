# Strings are immutable
a = "sohaib"
print(a.upper())
a = "SOHAIB"
print(a.lower())
a = "sohaib!!"
print(a)
print(a.rstrip("!"))
a = "sohaib"
print(a.replace("sohaib","sohail"))
a = "md sohaib"
print(a.split(" "))
Heading = "introduction to myself"
print(Heading.capitalize())
a = "Welcome to my world"
print(len(a))
print(a.center(38)) 
a = "This is my house.My house is so beautiful"
print(a.count("house"))
a = "Python is interpretd language"
print(a.startswith("Python"))
print(a.endswith("language"))
a = ("Welcome to the console")
print(a.endswith("to",4,10))
print(a.endswith("the",0,14))
a ="His name is Dan.He is an honest man"
print(a.find("is")) 
print(a.find("iss")) # ~>shows '-1' in output
print(a.index("name"))
# print(a.index("namee") ~> it shows an error
a = "welcometotheconsole"
print(a.isalnum())
print(a.isalpha())
a = "12345"
print(a.isalnum())  
a= "welcome145"
print(a.isalnum())
a ="welcome"
print(a.islower())
a= "WELCOME"
print(a.isupper())
a ="We wish you a Happy birthday"
print(a.isprintable())
a = "We wish you a Happy birthday\n"
print(a.isprintable()) 
a = "       "   # ~> using space
print(a.isprintable())
a = "       "  # ~> using tab
print(a.isprintable())
a = "World Health Organization"
print(a.istitle())
a = "world health organization"
print(a.istitle())
a = "His name is Dan. Dan is an honest man."
print(a.istitle())
a = "Python Is An Interpreted Language"
print(a.swapcase())