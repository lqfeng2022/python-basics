class Animal(object):
    def __init__(self):
        print("Animal constructor")
        self.age = 1


class Cat(Animal):
    def __init__(self):
        # Use super() function to access the base class
        super().__init__()
        print("Cat constructor")
        self.color = "Black"


cat = Cat()
print(cat.age)
print(cat.color)
