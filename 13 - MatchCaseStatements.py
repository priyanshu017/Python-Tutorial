# To implement switch-case like characteristics very similar to if-else functionality, we use a match case in Python.
# A match statement will compare a given variable's value to different shapes, also referred to as the pattern.
# The main idea is to keep on comparing the variable with all the present patterns, until it fits into one.
# The match case consists of 3 main entities(the match keyword/one or more case clauses/expressions for each case).

x = int(input("Enter the number to match macha:")) #x is the variable to match
match x: #matches x
    case 0: #if x is 0
        print("X is zero")
    case 4 if x % 2 == 0: # case with if condition
        print("x % 2 == 0 and case is 4")
    case _ if x < 10: #Empty case with if-condition
        print ("X is < 10")
    case _: #Default case - only matched if the above cases were not matched
        print(x)
# Ek baar koi case match ho gaya to uske neeche ke cases match nahi hote.