# class MyCLass:
#     x = 5

# ss = MyCLass()
# s2 = MyCLass()
# print(s2.x)

# class MyPython:
#     y=8
#     x=3
# s = MyPython()
# s1 = MyPython()
# print(s.x,',',s.y)
# print(s1.x,',',s1.y)
# del s

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# # class EPerson:
# #     def _init_(self, name, age):
# #         self.name = name
# #         self.age = age
# # p1= EPerson("Sakshi",23)
# # print(p1.name)
# # print(p1.age)

# class Person:
#   pass

# p1 = Person()
# p1.name = "Tobias"
# p1.age = 25

# print(p1.name)
# print(p1.age)

# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# class Calculator:
#   def add(self,a, b):
#     return a + b

#   def multiply(self,a, b):
#     return a * b

# calc = Calculator()
# print(calc.add(a,b))
# print(calc.multiply(a,b))

# class Dog:  
#     def __init__(self, name):  
#         self.name = name

#     def bark(self):  
#         print(f"{self.name} says Woof!")  

# my_dog = Dog("Rex")
# print(my_dog.name)

# ## inheritance

# # parent class
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# x = Person("John", "Doe")
# x.printname()

# # child class
# class Student(Person):
#   pass
# x = Student("Mike", "Olsen")
# x.printname()


# ## polymorphism

# name=("Sakshi")
# print(len(name))

# ## encapsulation

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age) # This will cause an error


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

# p1 = Person("Tobias", 25)
# print(p1.get_age())


## inner class

class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
inner = outer.Inner()
# inner.display()
print(outer.name)
print(inner.display())

