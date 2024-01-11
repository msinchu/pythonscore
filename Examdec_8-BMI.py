#body mass index calculator
#BMI calculation
def BMI_relation(W,H):
    BMI=(W/1000)/(H/100)**2
    print("BMI :",BMI)
    if BMI <18.5:
        print("you are Underweight.")
    elif BMI>=18.5:
        print("you are Normal.")
    elif BMI<=24.9:
        print("you are Normal.")
    elif BMI>=25.0:
        print("you are Overweight.")
    elif BMI<=29.9:
        print("you are Overweight.")
    elif BMI>=30.0:
        print("you are Obesity.")

    
#collect datas from the user
W=float(input("enter your weight IN KG :"))
H=float(input("enter your height IN M : "))
A=float(input("enter your age :"))
G=str(input("enter your gender :"))
BMI_relation(W,H)
  