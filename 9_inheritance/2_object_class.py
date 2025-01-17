class Animal:
    def __init__(self):
        self.age = 1

    def catch(self):
        print("Catch catch")


class Cat(Animal):
    def meow(self):
        print("Meow meow")


# Instantiate a Cat obj
cat = Cat()

# Instance object checking
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))
print(isinstance(cat, object))

# Create an empty object
object_one = object()

# Subclass checking
print(issubclass(Cat, Animal))
print(issubclass(Cat, object))
