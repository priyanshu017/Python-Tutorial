#String Length, String Uppercase, String Lowercase
name = "Priyanshu!! !!Priyanshu!!!!"
print(len(name))

#concept of immutability - we cannot change the string in-place, jo initialize kar diya, wo nahi badalta. Par nayi string mil jaati hai, method se
print(name.upper()) #nayi string banti hai, existing string ko affect nahi karta - bas upper case ki string bana deta hai
print(name.lower()) #nayi string banti hai, existing string ko affect nahi karta - bas lower case ki string bana deta hai
print(name.rstrip("!")) #sirf trailing exclamation ko remove karta hai, leading ko strip nahi karega
print(name.replace("Priyanshu", "John")) #replaces all the occurences of a particular string, with another string
print(name.split(" ")) #Splits the given string at the specified instance and returns the separated string as list items

blogHeading = "introduction to js"
print(blogHeading.capitalize()) #Turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
print(blogHeading.center(36))  #Aligns the string to the center as per the parameters given by the user
print(len(blogHeading))
print(len(blogHeading.center(36)))

print(name.count("Priyanshu")) #Returns the number of times a given value has occured within the given string
print(name.endswith("!")) #The endswith() method checks if the string ends with a given value. If yes, then return True, else False.

print(blogHeading.endswith("!"))

strung = "Welcome to the console !!!"
print(strung.endswith("!!!")) #endswith - Returns True only if the string ends with the given character/value. Else False.
print(strung.endswith("to", 4, 10)) #We can also check for a value in-between the string by providing start and end index positions.

strong = "Guy's name is Dan. He is an honest man"
print(strong.find("is")) #Finds the first occurence of a given value and returns the index where it is present. If given value is absent, return -1.
print(strong.index("Dan")) #Index - searches for the first occurence of the given value and returns the index where it is present.
#Index and Find are similar, the difference is only that if a value is absent, find method returns -1, and index method raises an exception[valueError]

#Boolean value returning Methods
print(strong.isalnum()) #Isalnum - returns True only if the  entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, it returns False.
print(strong.isalpha()) #Isalpha - returns True only if the  entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, it returns False.
print(strong.islower()) #islower - returns True if all the characters in the string are lower case, else returns False.
print(strong.isprintable()) #isprintable - returns True if all the values in the given string are Printable, else False.
print(strong.isspace()) #isspace - Only returns True, if there are any white spaces " ". Else returns False.
print(strong.istitle()) #istitle - Returns True only if the the first letter of each word of the string is capitalized, else returns False.
print(strong.isupper()) #isupper - returns True if all the characters in the string are upper case, else returns False.
print(strong.startswith("Guy")) #startswith - returns True only if the string starts with the given character/value. Else False.

print(strong.swapcase()) #swapcase - changes upper case to lowercase and lower case to uppercase. Changes character casing.
print(strong.title()) #title - changes the first letter of each word in the string to Capital. Capitalizes the first letter of each word.

