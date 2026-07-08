# # from function import sum
# # sum(3,3)
# # sum(3,3)
# # sum(3,3)
# # sum(3,4)
# # import datetime
# from datetime import datetime

# x = datetime.now()
# print(x)

# def sum(a,b):
#     print(a+b)
# sum(10,20)

# from module import sum
# sum(1,2)
# sum(3,4)
# sum(4,5)
# sum(9,10)

# from datetime import datetime
# x=datetime.now()
# print(x.year)
# print(x.day)
# print(x.strftime('%W'))

## 
from page1 import page1


from datetime import datetime

year = 2026
odd = 0
even = 0
count = 0

for month in range(1, 13):

    if month == 2:
        days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        days = 31

    for day in range(1, days + 1):
        d = datetime(year, month, day)

        if d.weekday() == 5:
            count += 1

            if count % 2 == 0:
                even += 1
            else:
                odd += 1

print("Odd Saturdays :", odd)
print("Even Saturdays :", even)
print("Total Saturdays:", odd+even)


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

# json methods
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

## pip installation

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
import cowsay

cowsay.cow("Hello, Sakshi!")
# cowsay.tux("I am Tux!")
# cowsay.dragon("Welcome!")
# cowsay.kitty("hey Kitt")
# cowsay.trex("Python is fun!")
# cowsay.kitty("hey Kittu")

# cowsay.cow("Hello")
# cowsay.tux("Hello")
# cowsay.dragon("Hello")
# cowsay.trex("Hello")
# cowsay.stegosaurus("Hello")
# cowsay.kitty("Hello")
# cowsay.turkey("Hello")
# cowsay.beavis("Hello")
# cowsay.cheese("Hello")
# cowsay.daemon("Hello")
# cowsay.fox("Hello")
# cowsay.ghostbusters("Hello")
# cowsay.meow("Hello")
# cowsay.miki("Hello")
# cowsay.milk("Hello")
# cowsay.octopus("Hello")
# cowsay.pig("hey fattu")
# cowsay.stimpy("Hello")

print(dir(cowsay))