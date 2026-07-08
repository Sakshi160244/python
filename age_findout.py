# age findout

teenage = 0

for i in range(1, 6):
    age = int(input("Enter the age:"))

    if 1 <= age <= 11:
        print("child")
    elif 11 < age <= 19:
        teenage += 1
        print("teenage")
    elif 19 < age <= 30:
        print("youngster")
    elif 30 < age <= 60:
        print("parentage")
    else:
        print("oldage")

print("total teenage:", teenage)


