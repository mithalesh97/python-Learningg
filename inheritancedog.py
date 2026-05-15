# this is a basic level inheritance 
class Animal:
    @staticmethod
    def sound():
        print("animal produce sound!")

class dog(Animal):
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} barks!")

d = dog("seru")
d.sound()
Animal.sound()