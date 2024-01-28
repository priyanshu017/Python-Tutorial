questions=[["which language is used to create facebook?","Python","French","Javascript","PHP", "None", 4],["which city is the capital of India?","Pune","Delhi","Mumbai","Ghaziabad","Pakhnau",2],["who is the Current Prime Minister of India ?","Fadnavis","Nehru","Modi","Gandhi","Banerjee",3],["Who was brother of Lord Shri Rama","Pandavas","Laxman","Arjun","Duryodhan",2],["who is the owner of Jaguar?","Ratan Tata","Ambani - Mota bhai","Adani","Musk",1],["What is the capital of UP?","Pakhnau","Moradabad side","Zila Ghaziabad","Lucknow",4],["What is the name of the company that manufactures Camaro","Maruti","Chevrolet","Toyota","Tata",2],["When did India gain independence?","1947","Humein bas azadi se matlab hai","1835","2020",1]]
levels=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]

for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(question[0])
    print(f"1.{question[1]}  2.{question[2]}")
    print(f"3.{question[3]}  4.{question[4]}")
    reply = int(input("Enter your answer question(1-4):Or press 0 to quit: "))
    if (reply == 0):
        money=levels[i-1]
        print("Aaj aap yaha se apne ghar leke jaayenge :",money,"ki raashi")
        break
    if(reply == question[-1]):
        print(f"Sahi jaavaab, aap jeet-te hain {levels[i]}.","Aur ab hum chalte hain agle padhaav ki taraf")
        if(i == 4):
            money = 4000
        elif(i == 11):
            money = 320000
        else:
            print("Wrong answer, you are thrown out of the game!")
print("Total winning: ", money)
