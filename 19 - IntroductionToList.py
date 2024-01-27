# Easier referral, easier storage, easier manipulation, easier conditional statements to add. Ek naam ke andar, multiple related cheezein store karne ke liye.
"""
- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within Square brackets.
- Lists are changeable(mutable), it means, we can change them after creation.
"""
listo = [3, 5, 6, "Priyanshu", True, 2, 23, 32, 345, 22] #List can store multiple data-types.
print(listo)
print(type(listo))
print(listo[1]) # List Index, similar to String Index. Starts from 0, until (n-1), where n is the number of items.

#Negative Indexing - Similar to positive indexing, neagtive indexig is also used to access the items from the list.
print(listo[-3]) #Negative Indexing
print(listo[len(listo) - 3]) #Positive indexing for -3 index
print(listo[5 - 3]) #Positive Index
print(listo[2]) #Positive Index

# To find - if an element is in a list or not: Same thing applies for string as well.
if "Priyanshu" in listo:
    print("Yes")
else:
    print("No")

#To print all the elements of the list:
print(listo)
print(listo[:]) # With indexing bhi kaam karta hai, to hum slicing kar sakte hain.
print(listo[0:10:2]) # 2 here is jump index, to ek ek value skip karke har alternate value print karega.

#List comprehension: On the fly ek list ko generate kar rahe ho. Used for creating new lists from other iterables like lists, tuples, dictionaries, sets and even arrays and strings.
lst = [i*i for i in range(4)]
print(lst)
lste = [i*i for i in range(10) if i%2 == 0]
print(lste)
