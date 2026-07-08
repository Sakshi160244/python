#question.py
##ternary operator


# y=int(input(" enter the morning time",))
# z=int(input("enter the halft ime",))
# k=int(input ("enter the exit time",))
#i="present" if y==8 & z>=18 else "absent" "halftime" if y==8 & z>=13 else " " "overtime" if y==8 & z<18 else "absent"
#print(i)
# j= "present","halftime" if y==8 and z>=13  else "absent"
# print(j)
# l= "full day "if y==8 and k<=18 else "overtime"
# print(l)

morning = int(input("Enter Morning Time = "))
evening = int(input("Enter Evening Time = "))
if morning <= 8 and evening == 18: 
     print("Present")
elif morning <=8 and evening >=18:
        print("overtime")
elif morning <=8 and evening ==13 or morning <= 13 and evening == 18:
        print("Half Day") 
elif morning >=8 and evening <=13 or morning >=13 and evening <=18:
        print("short Day")
else:
        print("no") 



