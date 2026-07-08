#practice question.py

#1 write a Python program to store your name, age , and city in variables and print them.
name="my name is Sakshi"
age= "i m 23 years old"
city="i live in sonipat"
print(name,age,city)
print(name)
print(age)
print(city)

#2 how do you create a string in python? give two examples.
print("hello! Good afternoon")


x="fruits name"
y="banana","apple","grapes"
print(x)
print(y)

a='vegetables name'
b="""patato,onion,
chilli,tamato,"""
print(a)
print(b)

#3 what are arithmetic operators in python? list any four.
print("Arithmetic operators are +,-,*,/,%,**,//")
x=10
y=20
print("add of two no.:",x+y)
print("sub of two no.:",y-x)
print("mul of 2no.:",x*y)
print("div of 2no.:",y/x)
print("mod of no.:",y%x)

#4 write a program to check if a no. is positive or negative.
num=int(input("eneter a no.:"))
if num>0:
    print("no. is positive")
else:
    print("no. is negative")


#5 write a program to check if a person is eligible to vote(age>=18).

age=int(input("enter the age :"))
if age>=18:
    print("eligible")
else:
    print("not eligible")

#6 create a varisble name and store your name in it . print the variable.
name="Sakshi"
print(name)

#7 create two variables a=10 and b=20 print their sum.

a=10
b=20
c=a+b
print(c)
print(a+b)

#8 store your age in a variable and print:"my age is 18"(replace 18 with your age).

age=18
print(age.replace("My age is 18","My age is 23"))
print(age.replace("18","23"))

#9 create variable for the marks of 5 subjects and calculate the average.

h=int(input("enter the marks of 1st subject:"))
e=int(input("enter the makrs of 2nd subject:"))
m=int(input("enter the marks of 3rd subject:"))
s=int(input("enter the marks of 4th subject:"))
c=int(input("enter the marks of 5th subject:"))
print(h,e,m,s,c)
v=(h+e+m+s+c)/5
print("calculate the average:",v)


#10 find the difference between 50 and 18.

x=50
y=18
print("difference between x and y :",x-y)







