#Strings - anything that you enclose between single or double quotation marks is considered a String. 
# A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
name = "Priyanshu"
friend = "Indu"

#double quotes ke andar double quotes - using Escape
apple = "He said, \"I want to eat an apple\""

#or
banana = 'He said, "I want to eat a banana"'

#multi-line string - either using triple single/double quotes('''abcd'''/"""mereku aa gaya""")
pomegranate = '''Hey Bro
I want to eat
Some pomegranate'''

anotherFriend = "Vijay"
print("Hello, " + name)

# Indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[9]) #IndexError: string index out of range - kyuki 9 index par kuch nahi hai.


