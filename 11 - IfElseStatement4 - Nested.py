#Nested if statement - We can use if, if-else, elif statements inside other if statements as well.
num = int(input("Enter your preferred number: "))
print("Voila! The number you entered is: ", num)
if (num < 0):
    print("Number is negative")
elif(num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("The number is greater than 20")
else:
    print("Number is zero, nyit")
print("Zindadil print statement")
