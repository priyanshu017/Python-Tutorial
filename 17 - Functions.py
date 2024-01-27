# Har cheez ka ek function bana ke use kahin bhi use kar sakte hain.
# This is a way to use a single block of code in multiple locations. Increases reusability.
# Function is a block of code, which perform a specific task whenever it is called. 

aMean = int(input("Enter the first number: "))
bMean = int(input("Enter the second number: "))
gmean = (aMean*bMean)/(aMean+bMean)
print(gmean)

# Ab agar c aur d 2 aur number ka mean nikaalna hoga to fir aur dikkat. Fir se codelikhna padega. To best way to execute is function.

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater")

def isLesser(a,b):
    pass #Jab humein pata hai ki hum code baad mein likhenge. To ye keyword use karte hai, so that Python knows it has to execute other blocks of code.

a = int(input("Enter the mean first: "))
b = int(input("Enter the mean second: "))
calculateGmean(a,b) #Calling function, Geometric Mean - values pass karo, aur call kar do uske baad
isGreater(a,b) #Calling function, is greater.

"""
2 types of Functions:
1. Built-in functions: These functions are defined and pre-coded in Python. Examples: min(), max(), sum(), type(), range(), dict().
https://docs.python.org/3/library/functions.html
2. User defined functions: We can create specific functions in python to perform tasks as per our needs. Such functions are user-defined.
"""