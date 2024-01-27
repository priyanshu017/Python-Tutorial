# How can we manipulate/modify a list in Python.
listo = [11, 45, 1, 2, 4, 6]
print(listo) # Prints the list
listo.append(7) # Adds the  value to a new index in list, highest index considered. Adds the value, to the end of the list.
print(listo)
listo.sort() # Sorts the list in ascending order.
print(listo)
listo.sort(reverse=True) # Sorts the list in descending order, seedhe sort kar ke reverse kar deta hai.
print(listo)
listo.reverse() # Reverses the list in its current state.
print(listo)
print(listo.index(1)) # List mein agar '1' hai, to uska index de dega.
print(listo.count(7)) # List mein kitni baar '7' hai, uska count bata dega.
misto = listo # The list stays the same, only the reference is copied.
misto[0] = 0 # This change wold affect the lists, since the list item is changed anyway. When we set, misto = listo, only the reference of the list is copied.
print(listo)
print(misto)
misto = listo.copy() # For copying, we should use this, since it creates a new list instance.
misto[0] = 35 # Here, the new list will be updated, the existing list will stay untouched.
print(listo)
print(misto)
listo.insert(1, 899) # Inserts the value 899 at index 1. This is done when we needs to insert(append) some value at a particular index.
print(listo)
print(misto)
listo.extend(misto) # Adds another list, or any other collection datatype(tuple, set, dictionary) to the existing list.
print(listo)

# Concatenating two lists.
m = [900, 1000, 1100, 3500]
print(m)
k = listo + m # This is used, if we need the result of the extend function, but we don't want to make changes to our existing list(listo).
print(k) 