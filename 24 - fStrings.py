# Helps place variables in Python. Can be done in python using the format method.

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Priyanshu"
print(letter.format(name, country))

print(f"Hey my name is {name} and I am from {country}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
bext = f"For only {{price:.2f}} dollars" #Retaining the f-string as the f-string.
print(bext)