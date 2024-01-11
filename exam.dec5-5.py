unit=int(input("Enter the unit consumed :"))
if unit<=100:
    print("No charge")
if 100<=unit<=200:
    amount=unit-100*5
    print("Amount is",amount)
elif unit>=200:
    amount=100*0+100*5+(unit-200)*10
    print("Amount is",amount)
else:
    print("invalid unit")