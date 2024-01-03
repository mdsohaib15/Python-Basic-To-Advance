# 1-Union() and update():
# The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.
print("1-Union() and update")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo",  "Madrid","Seoul", "Kabul"}
cities3 = cities1.union(cities2)
print(cities3)

# Update():
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
print(cities1)
cities1.update(cities2)
print(cities1)

# 2-Intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
print("\n2-Intersection")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
cities3 = cities1.intersection(cities2)
print(cities3)

print("\nintersection_update")
cities1.intersection_update(cities2)
print(cities1)

# # 3-Symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
print("\n3-Symmetric_difference")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)
print("\nsymmetric_difference_update")
cities1.symmetric_difference_update(cities2)
print(cities1)

#4- Difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
print("\n4-Difference")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
cities3 = cities1.difference(cities2)
print(cities3)
print("\ndifference_update")
cities1.difference_update(cities2)
print(cities1)