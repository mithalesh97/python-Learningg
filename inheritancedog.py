class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

class GuideDog(Dog):
    def __init__(self, name, breed, owner):
        super().__init__(name, breed)
        self.owner = owner

    def guide(self):
        print(f"{self.name} is guiding {self.owner}")

g = GuideDog("Rex", "Labrador", "Milan")
g.speak()
g.guide()
print(g.name, g.breed, g.owner)