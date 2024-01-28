# Tuples are immutable, so if we need to change a tuple, we would need to convert it to a list and then again convert it to a tuple.
# We will only be performing the operation on the list, and then again convert it to a tuple.
countries = ("India", "Italy", "France", "Russia", "Israel", "Australia", "Vietnam")
temp = list(countries)
temp.append("Japan")
print(temp)
temp.pop(3)
print(temp)
temp[2] = "Finland"
print(temp)
countries = tuple(temp)
print(countries)

# However, we can concatenate two tuples, since we are creating a new tuple and not manipulating existing tuples.
countries2 = ("New Zealand", "South Korea", "Iran", "Germany", "Netherlands")
mergeCountries = countries + countries2
print(mergeCountries)

# Count Method
tuple1 = (0, 1, 2, 3, 2, 4, 5, 1, 3, 5, 2, 5 , 2, 4, 2)
res = tuple1.count(3)
print("Count of 3 in tuple1 is: ", res)
#Index method:
bes = tuple1.index(3) #index method, used to find the index of a particular value. Agar nahi mili value to ValueError maarega.
print("The first occurence of 3 in tuple1 is at index: ", bes)
nes = tuple1.index(3, 4, 10) # Finding the index of 3 between Index 4 and 10. Agar nahi milegi value, to ValueError dedega.
print("The occurence of 3 between, index 4 and 10 is at index: ", nes)