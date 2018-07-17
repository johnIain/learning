class Dog() :
    def Eat(self):
        pass
    def Run(self):
        pass
class Usedog(Dog):
    def Eat(self):
        print("Dog is eatting!")
    def Run(self):
        print("Dog is running!")
class Abstractactory():
    def Action(self):
        pass
class Factory(Abstractactory):
    def Getfactory(self):
        return Usedog()
def client():
    factory=Factory()
    a=factory.Getfactory()
    a.Eat()
    a.Run()
client()
