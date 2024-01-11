#write a python program that executes an operation on a list and handles an indexError exception if the index is out of range.
def list_p(list,index):
    try:
        print("element=",list[index])
    except IndexError as e:
        raise Exception("index is outof range",e)

limit=int(input("enter the limit :"))
list=[]
for i in range(limit):
    num=int(input("enter the numbers :"))
    list.append(num)

print("list elements are :",list)
index=int(input("enter the index of element you want :"))
list_p(list,index)