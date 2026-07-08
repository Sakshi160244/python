# #operat.py

# # # arthematic operator
# a=10
# b=20
# c=30
# print("sum of two variables",a+b)
# print("sub of two variables",a-b)
# print("mul of two variables",a*b)
# print("div of two variables",a/b)
# print("modulus of two variables",c%a,c%b)
# print("exponent of variable",a**b)
# print("floor division of the variable",b//a,c//a)

# # ##assignment operator

# x=5
# x+=10
# print(x)
# x-=2
# print(x)
# x*=4
# print(x)
# x/=5
# print(x)
# x%=20
# print(x)
# x//=2
# print(x)
# x**=3
# print(x)

# ##comparision operator

# x=5
# y=10
# print(x==y)
# print(x==y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)


# ## chaining comparison operator

# x=10
# print(x)
# print(1<x<10)
# print(1<x and x<10)


# x=5
# print(x>3 and x<10)
# print(x)

# # question

# marks=int(input("enter the marks:"))

# if 100>=marks>=80:
#     print("Grade A")
# elif 80>marks>=60:
#     print("Grade B")
# elif 60>marks>=45:
#     print("Grade C")

# else:
#     print("Fail")


# # if a number is divisible by 2 and 5 
num2=0
num5=0
for i in range(1,6):
    num=int(input("enter the number is divisible by 2 and 5:"))

    if num%2==0 and num%5==0:
        print("no. is divisible by both 2 & 5")
    elif num%2==0:
        print("no.is divisible by 2")
        num2+=0
    elif num%5==0:
        print("no. is divisible by 5")
        num5+=0
    else:
        print("not divisible by 2 and 5")
print("total no. which is divisible by 2:",num2)
print("total no. which is divisible by 5:",num5)

# age findout

# teenage=0
# for i in range(1,6):
#     age=int(input("enter the age:"))

#     if 1<=age<11:
#         print("child")
#     elif 11<age<=19:
#         teenage+=1
#         print("teenage")
#     elif 19<age<=30:
#         print("youngster")
#     elif 30<age<=60:
#         print("parentage")
#     else:
#         print("oldage")
# print("total teenage:",teenage)


