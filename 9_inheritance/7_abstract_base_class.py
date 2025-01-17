# 1)Import ABC class and abstractmethod func
from abc import ABC, abstractmethod


class AppleExistsError(Exception):
    pass


# 2)AppleRecipe -> ABC
class AppleRecipe(ABC):
    def __init__(self):
        self.has_apples = False

    def buy_apples(self):
        if self.has_apples:
            raise AppleExistsError("Apples' enough")
        self.has_apples = True

    def finish_apples(self):
        if not self.has_apples:
            raise AppleExistsError("There's no apple")
        self.has_apples = False

    # 3)cook(): interface
    @abstractmethod
    def cook(self):
        pass


class ApplePie(AppleRecipe):
    def cook(self):
        print("Make apple pie")


# Concrete child class
class AppleCake(AppleRecipe):
    def cook(self):
        print("Make apple cake")


# Abstract child class
class AppleSalad(AppleRecipe):
    pass


recipe = ApplePie()
recipe.cook()
