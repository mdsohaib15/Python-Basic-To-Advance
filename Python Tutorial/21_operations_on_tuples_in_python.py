countries = ("Spain", "Italy", "India", "England", "Germany")
print(countries)
countries_list = list(countries)
print(countries_list)
print("append")
countries_list.append("Russia") # add item
countries = tuple(countries_list)
print(countries)
print("pop")
countries_list.pop(3) #remove item
countries = tuple(countries_list)
print(countries)
print("change")
countries_list[2] = "Finland" #change item/replace item
countries = tuple(countries_list)
print(countries)

print("Concatenating:")
# we can directly concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)