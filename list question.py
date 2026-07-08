# list comprehension

# name=["neeru","charu","sakshi","chetna","vaishalli","partibha","chaaya","rinky","chanda","deepti","chiku"]
# newlist=[]
# for x in name:
#     if "c" in x:
#         newlist.append(x)
# print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)