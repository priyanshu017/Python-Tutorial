# Used for repetitive tasks, baar baar thodi na karenge repeat. Uske liye use karenge Loops. Types: For loops, While Loops, Nested Loops.
# Sometimes a programmer has to execute a group of statements a certain number of times. This can be done using Loops.

# For Loop - can iterate over a sequence of iterable objects in Python. Iterating over a sequence, is nothing but iterating over Strings, Lists, Tuples, Sets and Dictionaries.
name = "Priyanshu"
for i in name:
    print(i)
    if (i == "y"):
        print("This is something special")

colors = ["Red","Green","Blue","Yellow","Grey","Orange"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#Range - very important for FOR loop. Useful, if we do not want to iiterate over a sequence.
for k in range(5):
    print(k+1)

# Only the lower limit in the range is considered, upper limit is not included. The below function prints value from 1 to 20.
for j in range(1,21):
    print(j)

#Also, with the range function, we can set the repetition as well, like how the values repeat. This detail is added after the range specification.
for m in range(0, 21, 2):
    print(m)