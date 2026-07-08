#menucafe
print("Welcome to my Cafe:")
menu={"coffee":120,"pizza":200,"burger":100,"cold drink":80}
print("menu:",menu)
n=int(input("enter the items:"))
order={}
for i in range(n):
    item=input("items:")
    if item in menu:
        qty=int(input("enter the qty:"))
        order[item]=qty
    else:
        print("item not in menu.")
    subtotal=0
    for item,qty in order.items():
        subtotal+=menu[item]*qty
gst=subtotal*0.18
total=subtotal+gst
print("subtotal:",subtotal)
print("your gst cahrges:",gst)
print("your final bill:",total)
print("Thank you for visiting our Cafe.")
