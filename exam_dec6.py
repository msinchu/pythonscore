list=[]
user_input = int(input("enter the number of elements :"))
for i in range(user_input):
    number = int(input("enter the number :"))
    list.append(number)
print(list)
variable=True
while variable:
    i = 0
    variable = False
    while i<len(list)-1:
        if list[i]>list[i+1]:
           list[i],list[i+1]:
           variable=True
        i+=1
third_largest=list[-3]
print(f'third largest number:{third_largest}')




    