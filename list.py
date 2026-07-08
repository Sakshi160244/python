# # list.py

# # create a list 
# s=["sakshi","vishant","priyanshu","geeta","lavit","rishabh"]
# print(s)

# # list items are changeable and oderable and mutuable and allow duplicates

# # allow duplicates
# s=["sakshi","vishant","priyanshu","geeta","lavit","rishabh","geeta","lavit","sakshi"]
# print(s)

# #list length
# s=["sakshi","vishant","priyanshu","geeta","lavit","rishabh","geeta","lavit","sakshi"]
# print(len(s))
# print(type(s))

# # access items
# s=["sakshi","vishant","priyanshu","geeta","lavit","rishabh","geeta","lavit","sakshi"]
# print(s[2:9])
# print(s[0])
# print(s[-1])
# print(s[-7:-1])
# print(s[2:])
# print(s[:8])
# print(s[-2:])
# print(s[:-6])

# # check if items exists

# fruits=["apple","banana","kiwi","orange","mango","blueberry","lichi","papaya"]
# if "kiwi" in fruits:
#     print("Yes, 'kiwi' is in the fruits list")

# # change list items
# fruits=["apple","banana","kiwi","orange","mango","blueberry","lichi","papaya"]
# fruits[1]="bananas"     # change item value
# fruits[1:3]=["cherry","watermelon","melon"]     # change a range of item values
# print(fruits)

# ## add list items

# # insert items
# a=["cloths","bags","electronics","machnicals","networking"]
# a.insert(3,"mechnical")
# print(a)

# # append list items
# veg=["patato","tamato","chilli","onion"]
# veg.append("karela")
# print(veg)

# # extend list
# fruits=["apple","banana","kiwi","orange","mango","blueberry","lichi","papaya"]
# veg=("patato","tamato","chilli","onion")
# fruits.extend(veg)
# print(fruits)

# ## remove list items
# veg=["patato","tamato","chilli","onion"]
# veg.remove("chilli")    # sepecific item
# print(veg)

# # specific index item remove to use pop()
# fruits=["apple","banana","kiwi","orange","mango","blueberry","lichi","papaya"]
# fruits.pop(2)
# fruits.pop()
# print(fruits)

# # del 
# fruits=["apple","banana","kiwi","orange","mango","blueberry","lichi","papaya"]
# del fruits[3]
# del fruits[1:3]
# print(fruits)

# #clear
# fruits=["apple","banana","kiwi","orange","mango","blueberry","lichi","papaya"]
# fruits.clear()
# print(fruits)


# ##loop lists
# # loop through a list
# list=["hello","welcome","world"]
# for x in list:
#     print(x)

# # loop through the index numbers
# list=["hello","welcome","world"]
# for x in range(len(list)):
#     print(list[1])

# ## list comprehension
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
#     if "n"in x:
#         newlist.append(x)
# print(newlist)\

# #question in list comprehension
# name=["neeru","charu","sakshi","chetna","vaishalli","partibha","chaaya","rinky","chanda","deepti","chiku"]
# newlist=[]
# for x in name:
#     if "c" in x:
#         newlist.append(x)
# print(newlist)

# ## sort method
# fruits=["apple","banana","cherry","kiwi","mango"]
# fruits.sort()
# print(fruits)

# num=[100,50,65,82,23]
# num.sort() # sort in ascending order
# num.reverse() # sort in descending order
# print(num)

# num1=[100,50,65,82,23]
# num1.sort(reverse=True) # sort in descending order
# print(num1)

# copy list
veg=["patato","tamato","chilli","onion"]
fruits=veg.copy()
print(fruits)

#slice copy
veg=["patato","tamato","chilli","onion"]
fruits=veg[1:3]
print(fruits)

# # join list
# list1=[12,13,14,15,16,17,18]
# list2=[1,2,3,4,5,6,7,8,9]
# list=list2+list1
# print(list)