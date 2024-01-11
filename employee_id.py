class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def display(self):
    #     print("name is :",self.name,"age is :",self.age)


class Fam(Person):
    # def display(self,employee_id):
    #     print("employee_id is :",self.employee_id)
    def display(self,empid):
        self.empid=empid
        print("employee_id is :",self.empid,"employeename is :",self.name)

p2=Fam("sinchu",20)
p2.display(101)