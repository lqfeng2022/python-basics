class Animal:
    def greet(self):
        print("Animal greet")


class Pet:
    def greet(self):
        print("Pet greet")


class Cat(Animal, Pet):
    pass


cat = Cat()

# greet() calling flow: Cat -> Animal -> Pet
cat.greet()


# ------------------------------------------------------------
# A good example of multiple Inheritance:
class Hunter:
    def hunt(self):
        print("Hunt hunt")


class Companion:
    def companion(self):
        print("Be a companion")


class Cat(Hunter, Companion):
    pass
