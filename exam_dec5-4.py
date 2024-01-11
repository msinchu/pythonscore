bike=str(input("enter the name of the bike :"))
price=float(input("enter the cost price of the bike :"))
x=price*(15/100)
y=price*(10/100)
z=price*(5/100)
if price>100000:
    print(x)
elif price>50000:
    print(y)
elif price<100000:
    print(y)
elif price<=50000:
    print(z)