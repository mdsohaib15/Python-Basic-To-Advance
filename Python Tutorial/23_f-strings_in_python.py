## String formating:
letter = "Hey my name is {0} and I am from {1}"
name = "Sohaib"
country = "Pakistan"
print(letter.format(name,country))

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.29455))

## f-strings in python:
name = "Sohaib"
country = "Pakistan"
print(f"Hey my name is {name} and I am from {country}")
print(f"{2*30}")