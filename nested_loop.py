# nested loop
# present = 0
# absent = 0
# overtime = 0
# half_day = 0
# short_day = 0
# weekdays=0
#grandtotal=0
grand_total_present = 0
grand_total_absent = 0
grand_total_half_day = 0
grand_total_short_day = 0
grand_total_overtime = 0

for i in range(1,3):
    present = 0
    absent = 0
    overtime = 0
    half_day = 0
    short_day = 0
    weekdays=0
    

    
    for j in range(1,3):
        
            morning = int(input("Enter Morning Time = "))
            evening = int(input("Enter Evening Time = "))
            if j ==6:
                    print("it's a weakday")
                    weekdays+=1
                
            elif morning <= 8 and evening == 18:
                    print("Present")
                    present += 1
                    grand_total_present += 1
                
            elif morning <=8 and evening >=18:
                    print("overtime")
                    overtime +=1
                    grand_total_overtime += 1
                    
            elif morning <=8 and evening ==13 or morning <= 13 and evening == 18:
                    print("Half Day") 
                    half_day +=1
                    grand_total_half_day += 1
                    
            elif morning >=8 and evening <=13 or morning >=13 and evening <=18:
                    print("short Day")
                    short_day +=1
                    grand_total_short_day += 1
                
            else:
                    print("absent") 
                    absent += 1
                    grand_total_absent += 1
                
        
    print("weekday:",weekdays)
            
    print("total present =", present)
    print("total absent =", absent)
    print("total overtime =", overtime)
    print("total half_day =", half_day)
    print("total short_day =", short_day)
    
    
print("grand total present =", grand_total_present)
print("grand total absent =", grand_total_absent)
print("grand total overtime =",grand_total_overtime)
print("grand total half_day =", grand_total_half_day)
print("grand total short_day =",grand_total_short_day)




