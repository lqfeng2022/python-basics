class Animal:
    # Create the age attribute
    def __init__(self):
        self.age = 1

    def catch(self):
        print("Catch catch")


class Cat(Animal):
    def meow(self):
        print("Meow meow")


# Instantiate a Cat obj
cat = Cat()

cat.catch()
print(cat.age)
