#@ string.py
#type casting
# t=int(input("enter the rate of tshirt:"))
# j=int(input("enter the rate of jeans:"))
# s=int(input("enter the rste of shoes:"))
# sub_total=float(t+j+s)

# total=str(sub_total)
# print(total)

## match 
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

day = 6
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")