##tuple
# oderable, unchangeable, allow duplicates,immutable
my=("sakshi","chiku","lavit","vishant","geeta","parul","sakshi","chiku","geeta")
print(my)
print(len(my))
print(type(my))

m=("sakshi",) # tuple with one item
print(m)

n=(True,False) #boolean tuple
print(type(n))

n=(1,2,3,4,5,6,7,8,9) # integer tuple
print(n)
print(type(n))

n=(1.5,2.5,3.5,4.5,5.5) # float tuple
print(type(n))

s=tuple(("sakshi","vishant",)) #tuple constructor
print(s)

x=("apple","banana","kiwi","orange","mango","blueberry","lichi","papaya")
print(x[2])
print(x[-5])
print(x[2:])
print(x[:6])
print(x[0:-3])
print(x[0:8])

# tuple are not changeable , not remove items and not add items 
#tuple items are change then convert into a list and then change the ittems and again convert into a tuple
x=("apple","banana","kiwi","orange","mango","blueberry","lichi","papaya")
y=list(x)
y[3]="grapes"
x=tuple(y)
print(x)

x=("apple","banana","kiwi","orange","mango","blueberry","lichi","papaya")
y=list(x)
y.append("guava")
x=tuple(y)
print(x)
y.remove("orange")
x=tuple(y)
print(x)
del y[7]
x=tuple(y)
print(x)

# packin and unpacking tuple
veg=("patato","tamato","chilli","onion")
print(veg)      #packing tuple
(apple,*banana,mango) = veg
print(apple)
print(banana) #unpacking tuple

## loop tuple
a=("A","B","C","D")
for x in a:
    print(x)
    for x in range(2):
        print(a[x])

##join tuple
t1=(1,2,3,4,5)
t2= ("bus","car","bike","cycle","bus","car","car","bus","cycle")
t=t1*3
t3=t1+t2
print(t3)
print(t)
print(t2.count("car"))
print(t2.index("car"))

