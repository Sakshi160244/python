#chatbot
##chatbot choice
bot={"1":"hey","2":"bye","3":"would you like tea & coffee","4":"please repeat again"}
print(bot)

while True:
    
    
    for i in bot:
        press=int(input("enter the number:"))
        #for i in bot:
        if press==1:
                print("bot:",bot["1"])
        elif press==2:
                print("bot:",bot["2"])
        elif press==3:
                print("bot:",bot["3"])
        elif press==4:
                print("bot:",bot["4"])
        else:
                print("invalid input")
                break
    break
    

       