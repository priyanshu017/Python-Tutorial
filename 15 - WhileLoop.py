for i in range(3):
    print(i)
#above FOR loop implementation, done below, using the While Loop.
i=0
while(i<3):
    print(i)
    i = i + 1
print("Zindadil Print")

#Checking for a condition, and only if the condition is false, will the while loop exit, until then, it's going to keep cooking.
i = int(input("Enter the number: "))
while(i <= 38):
    i = int(input("Enter the number again bro: "))
    print(i)
print("Zindadil Print Statement")

#decrementing while loop - dheere dheere kam hoti reh rahi hai value, aur jab condition false ho jaayegi to bas done, ho gaya, khatam loop.
count = 5
while (count > 0):
    print(count)
    count = count - 1
else: # Else can also be used with While Loop, to execute else, if the condition becomes false, then else is executed.
    print("I am inside else")
print("Desi Zindadil Print")

# Do-while loop is there is other languages, but doesn't exist in Python. Question - Emulate do-while loop in Python. [IMPORTANT]. Kam se kam ek baar execute to hoga hi.
while True:
    number = int(input("Enter the number - is equal to number: "))
    print(number)
    if not number < 38:
        break
print("Zindadil print statement - bole to hardam print hone ka")