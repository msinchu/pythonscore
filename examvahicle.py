class Vahicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print("the make is :",)
    
class Car(Vahicle):
     def start(self,num_doors):
         self.num_doors=num_doors
         print("car make is :",self.make,"car model is :",self.model,"number of doors is :",self.num_doors)
     def stop(self):
         print("thank you for visiting our office :",self.make)

class Motorcycle(Vahicle):
    def start(self,two_wheels):
        self.two_wheels=two_wheels
        print("motor cycle make is :",self.make,"motorcycle model is :",self.model,"company of two wheels is",self.two_wheels)
    def stop(self):
        print("thank you for visiting our office :",self.make)

c1=Car("Audi","2023A6",4)
c2=Car("Audi")
c1.start()
c2.stop()

m1=Motorcycle("Royal enfield meteor 350","supernova variant","royal enfield bulletalloy wheel")
m2=Motorcycle("Royal enfield")
m1.start()
m2.stop()