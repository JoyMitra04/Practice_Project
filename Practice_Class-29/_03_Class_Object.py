class Person:
    name = None
    age = None
    height = None
    weight = None

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def getpersonDetails(self):
        print("................")
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print("................")




Joy = Person("Joy Mitra", 20, 5.4, 59)
Joy.getpersonDetails()


samrat = Person("Samrat", 20, 5.6, 63)
samrat.getpersonDetails()
