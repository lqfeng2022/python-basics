from abc import ABC, abstractmethod


class AppleRecipe(ABC):
    @abstractmethod
    def cook(self):
        pass


class ApplePie(AppleRecipe):
    def cook(self):
        print("Make apple pie")


class AppleCake(AppleRecipe):
    def cook(self):
        print("Make apple cake")


# cook(): takes a list of objects
def cook(recipes):
    for recipe in recipes:
        recipe.cook()


apple_pie = ApplePie()
apple_cake = AppleCake()
cook([apple_pie, apple_cake])
