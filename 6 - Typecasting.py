#Change the data type of a variable to another, String to INT, INT to Str, and so on...
a = "Bro"
b = "Chill"
print(a + b)

#The conversion of one data type into another data type is known as type casting or type conversion in python.
c = "2"
d = "1"
print(c+d)

#Explicit Typecasting - we have to write the program/code - done manually - by developer/programmer
print(int(c)+int(d))

#Implicit Typecasting - done exclusively by Python itself. Bhaiya ji hum aapke liye kar dete hain Typecasting.
"""
Data types in Python do not have the same level i.e. ordering of data types is not same in Python. 
Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types,
in Python, one of the variable's data type will be changed to the higher data type. According to the level, one data type is converted into
other by the Python interpreter itself(automatically). This is called, Implicit typecasting in Python.

Python converts a smaller data type to a higher-data type, according to the level. To ensure there is no data loss.
"""
e = 1.9
f = 8
g = e+f
print(e+f)
print(type(g))
# here g is automatically typecasted to float, to ensure there is no data loss.
