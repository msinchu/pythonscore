class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("welcome to inheritance")

class Dog(Animal):
    def speak(self):
        print("says bow!!!!!!!!",self.name)

class Cat(Animal):
    def speak(self):
        print("says meow!!!!!!!!",self.name)

d=Dog("bella")
d.speak()

c=Cat("simba")
c.speak()
        