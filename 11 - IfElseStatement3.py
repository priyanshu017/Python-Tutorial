num = int(input("Enter the value of the number: "))
if (num < 0): #If this statement is true, python will run, what is inside the function and then exit the loop. Else, it will check the next condition.
    print("Number is Negative")
elif (num == 0): #Again, Python will check, True or False, and based on the condition, move on to the next function/exit.
    print("Number is Zero")
elif (num == 999): #Again, Python will check, True or False, and based on the condition, move on to the next function/exit.
    print("Number is special")
else: #Koi condition agar uppar true nahi hai, to bas ise hi true maan lega
    print("Number is Positive")
print("Zindadil print - kyuki, any way chalega, loop ke baahar hai")