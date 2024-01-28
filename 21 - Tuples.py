# Tuples are ordered collection of data items. They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets(). Tuples are unchangeable(immutable), so we cannot alter them after creation.

tuple1 = (1, 2, 3, 4, 5, 6, 6, 8)
tuple2 = ("Red", "Yellow", "Camaro", "Blue", "Mustang")
tuple3 = ("Koenigsegg") # If we do not add a comma, after the item, the default type of the item will be considered.
print(tuple1)
print(tuple2)
print(tuple3)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3)) # This will give the type as string, since tuple3 only has one item, no comma after the item and the type of item is string.

# Indexing in Tuple - similar to list. With positive and negative indexes working the same.
print(tuple1[3])
print(tuple2[4])

# Check for item in Tuple - similar to list. Done using the IF keyword.
if "Camaro" in tuple2:
    print("Camaro is a part of Tuple2")

# Slicing of Tuple is also possible. But, in this case, a new tuple is generated, the existing tuple is unaffected.
tuple4 = tuple2[0:3] # Only lower limit is considered, higher limit is not considered in the result. 
# ^^^ [[0:3] - Is Read as >= Index 0 and < Index 3]
print(tuple4)

# Printing all the elements from the start to the end of the tuple:
print(tuple4[0:])

# Print alternate values in the Tuple:
print(tuple1[0: :2]) # Here the " " after the first : is considered as the higher limit. If needed, we can also limit the result to aa particular index.

# Print every 3rd consecutive value within a given range:
print(tuple1[0:7:3])