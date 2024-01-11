#write a program to check whether the last digit of a number is divisible by 3
num=int(input("enter the numer :"))
x=num%10
y=x%3
if y==0:
    print("the last digit is divisible by 3")
else:
    print("not divisible by 3")