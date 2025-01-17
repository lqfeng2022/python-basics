class Animal:
    def catch(self):
        print("Catch catch")


class Mammal(Animal):
    pass


class Cat(Mammal):
    def meow(self):
        print("Meow meow")


# Siamese -> Cat -> Mammal -> Animal
class Siamese(Cat):
    pass
