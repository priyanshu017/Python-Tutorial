#String ke saath kaise khelte hain - playing with a string
name = "Priyanshu"
names = "Priyanshu,Indu,Vijay,Priyanka"
print(names[0:5]) #including 0 but not including 5
print(names[0:-9])
print(len(names))
fruit = "Mango"
length = len(fruit)
print(length)
print(fruit[:4])
print(fruit[:])

#negative slicing - peeche se negative index ko dekhta hai Python{ya to peeche se count karein, same index, ya fir len(variable) - 1/2/3/4}
fruit1 = "Pomegranate"
print(fruit1[0:-8])
print(fruit1[-1:-3])
print(fruit1[-3:-1])

#Quick Quiz
nm = "Priyanshu"
nmlength = len(nm)
print(nmlength)
print(nm[-4:-2])