import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hourTimestamp = time.strftime("%H")
print(hourTimestamp)
minuteTimestamp = time.strftime("%M")
print(minuteTimestamp)
secondTimestamp = time.strftime("%S")
print(secondTimestamp)

if (int(hourTimestamp) >= 4 and int(hourTimestamp) < 12):
    print("Good Morning my son!")
elif (int(hourTimestamp) >= 12 and int(hourTimestamp) < 16):
    print("Good Afternoon mere bache")
elif (int(hourTimestamp) >= 16 and int(hourTimestamp) < 19):
    print("Good evening beta")
else:
    print("Soja munna soja")
print("Zindadil print statement")

# To learn more - https://www.geeksforgeeks.org/python-strftime-function/
# To learn more and more - https://docs.python.org/3/library/datetime.html