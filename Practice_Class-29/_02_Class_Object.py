"""
1. Class
2. Object
3. Attribute

4. Constructor
5. Instance Method
"""

class Person:
    name = None
    age = None
    height = None
    weight = None

    def getDetails(self):
        print(".............")
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(".............")

Joy = Person()
Joy.name = "Joy Mitra"
Joy.age = 20
Joy.height = 5.4
Joy.weight = 59

samart = Person()
samart.name = "Smart"
samart.age = 20
samart.height = 5.6
samart.weight = 63

J = Joy
S = samart

J.getDetails()
S.getDetails()