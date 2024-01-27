# Kyu use karte hain break and continue?
#Loops work iteration by iteration, and we want the loop to exit on a particular iteration, or skip at a particular iteration and continue running the loop from next iteration.

#Break statement terminates the loop it lies within.

for i in range(12):
    if (i==10):
        break
    print("5X",i+1,"=", 5 * (i+1))
print("Chalo bete loop se baahar")

# Continue statement only skips one iteration, or any iteration based on the condition.
for j in range(12):
    if (j==10):
        print("Ye iteration skip hui")
        continue
    print("5X",j+1,"=", 5 * (j+1))
print("Zindadil Print Statement")