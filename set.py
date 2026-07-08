## set 
# set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# use {} to create a set
a={"sakshi",1,True,False,0,2,3,1.2,"panchal"}
print(a)
print(len(a))
print(type(a))

# access items 
a={"sakshi",1,True,False,0,2,3,1.2,"panchal"}
for x in a:
    print(x)
    for x in range(1,2):
        print(x)
# add items in set
x={1,2,3,4,5}
x.add(8)
print(x)
y={6,7,8,9,10}
x.update(y)
print(x)
z=[11,12,13,14,15]
x.update(z)
print(x)
a=("apple","banana","mango")
x.update(a)
print(x)

# remove items from sets
x={"mango","banana","apple","grapes","kiwi","banana"}
x.remove("banana") # if item not found then it will raise an error
print(x)
x.discard("guava") #if item not found then it will not raise an error
print(x)
x.pop() # remove a random item
print(x)
x.clear() # remove all items
print(x)    
# del x # delete the set
# print(x)

#loop set
y={"mango","banana","apple","grapes","kiwi"}
for x in y:
    print(x)
    for x in range(1,2):
        print(x)

# join sets
set1 = {"a", "b", "c","mango"}
set2 = {1, 2, 3}
set3={"mango","banana","apple","grapes","kiwi"}
set4={2.1,3.1,4.1}
set5={("apple","banana","mango")}
set6={"car","bus","bike"}
sets=set1|set2|set3|set4|set5|set6
print(sets)
set = set1.union(set2)
set=set1.union(set5)

print(set)

set1.update(set2)
print(set1)
set3.difference(set1)
print(set3)
set3.difference_update(set1)
print(set3)

#frozen set 
x={"apple","banana","mango","grapes","kiwi","apple"}

print(x)
set3.copy()
print(set3)

colors={"red","green","blue"}
print(colors)
colors.add("yellow")
print(colors)
colors.discard("green")
print(colors)
print(len(colors))

set=set5.intersection_update(set3)
print(set)