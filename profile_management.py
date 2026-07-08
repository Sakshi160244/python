##profile_management
#press 1 for old name and press2 for new name and press3 for old password and press4 for new password
a={"name":"Sakshi ","age":23,"city":"Sonipat","password":"sakshi123"}
for x in range(1,6):
    press=int(input("enter the no.:",))
    
    if press==1:
         print("old name is:",a["name"])
    elif press==2:
            a["name"]=input("enter the new name:")
            print("new name is :",a["name"])
    elif press==3:
            print("old password is:",a["password"])
    elif press==4:
            a["password"]=input("enter the new password:")
            print("new password is:",a["password"])
    else:
            print("invalid input")
