def average(a, b):
    print("The average is ", (a+b)/2)

average(4, 6)

# Types of Arguments: Default, Keyword, Variable length, and required arguments.

# Default arguments: We can provide a default value of the argument while creating a function. This way, the function assumes a default value, even if a value is not provided.
def averAge(num1 = 7, num2 = 5):
    print("The average is:", (num1 + num2)/2)
averAge(num2 = 13) #Ager bas ek value pass ki, to doosri default value se add ho jaayegi.

def name(fname, mname = "John", lname = "Kennedy"):
    print("Hello", fname, mname, lname)
name("Baba", "Bhootani")

# Keyword arguments - Order change kar sakte hain arguments ka:
# We can provide the arguments like "Key = value", when calling the function and in this case, the order doesn't matter, like averAge(num2 = 13)

# Required arguments: Adding a value is necessary, also, if there are multiple variables, with no value. 
# While adding value, if Keyword arguments are not used, the details should be passed in the same order.
def summation(j, k = 1): #Yaha j ki value is required. So it is a required argument, when calling the function.
    print("the sum is: ", j + k)
summation(11) # If the value of j is not given here, it would give an error.

# Variable-length arguments: Sometimes we need to pass more arguments than those defined in the actual function. This can be done using Variable length arguments.
# Arbitrary Arguments: While creating a function, pass a * before the parameter name, when defining the function.
# The function Accesses the arguments by processing them in the form of a tuple. 

def Average(*numbers):
    print(type(numbers))
    sums = 0
    for i in numbers:
        sums = sums + i
    print("Average is: ", sums / len(numbers))
Average(5,6)

# Keyword-arbitrary arguments: When creating a function, pass a ** before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of a dictionary. dict().
def naming(**names):
    print(type(names))
    print("Hello", names["fnames"], names["mnames"], names["lnames"])
naming(mnames="Buchanan", lnames="Barnes", fnames="James")

# Return statement: The return statement is used to return the value of the expression back to the calling function. BOHOTT ZAROORI.
def Averago(*nums):
    sumo = 0
    for khau in nums:
        sumo = sumo + khau
    return sumo / len(nums) #value ko leke vaapis chala jaata hai, calling function ke paas. Jaise wo tumhara dil leke apne Ex ke paas gayi thi.
scee = Averago(5,6,7,2)
print(scee)


