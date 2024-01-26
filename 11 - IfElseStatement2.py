applePrice = 210
budget = int(input("What is your budget: "))
if (applePrice <= budget):
    print("Alexa, add 1 Kg Apples to the cart")
else:
    print("Alexa, apples are way too costly for my pocket, keep them out of the cart")
print("Alexa: Done") #Indentation, is out of scope of the if/else function, so this will run anyway. Only the cde, inside the function, will run once the condition is met.

#elif statement - if we need to execute and check on more than one conditions.

mangoPrice = 250
mangoBudget = int(input("Enter the money in your pocket: "))
if (mangoBudget - mangoPrice > 50):
    print("Alexa ji, 1 Kg Mango add kar dein")
elif (mangoBudget - mangoPrice > 70): #Kyuki, iske uppar  wali statement True thi, ise execute nahi kiya Python snake
    print("Alexa chillar ke bhaav mein khareed lo")
else:
    print("Alexa main gareeb ho gaya hu kya?")

orangePrice = 250
orangeBudget = int(input("Enter jeb mein chavvani: "))
if (orangeBudget - orangePrice > 70):
    print("Alexa ji, 1 Kg Orange add kar dijiye")
elif (orangeBudget - orangePrice > 50): #Kyuki, iske uppar  wali statement False thi, Python is statement ko bhi check karega.
    print("Alexa chillar ke bhaav mein khareed lo")
else:
    print("Alexa ab bina oranges khaaye sona padega kya?")
