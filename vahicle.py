class Vahicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("welcome to mechinw world")

class Car(Vahicle):
    def display(self):
        print("Car brand is :",self.brand,"Car model is :",self.model)

class Motorcycle(Vahicle):
    def display(self):
        print("Motorcycle brand is :",self.brand,"Motorcycle model is :",self.model)

c=Car("Audi","2023A6")
c.display()

m=Motorcycle("Royal Enfield meteor 350","Supernova variant")
m.display()