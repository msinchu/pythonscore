try:
    a=int(input("enter the number :"))

    if a==0:
        print("the factorial of 0 is 1")
    factorial=1
    for i in range(a,1,-1):
        factorial=factorial*i
        print("the factorial of ",a,"is",factorial)
    
except:
    if a<0:
        raise Exception("factorial does not exit negative numbes")
