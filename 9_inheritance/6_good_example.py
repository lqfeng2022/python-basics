# 1)Create an exception class
class AppleExistsError(Exception):
    pass


class AppleRecipe:
    def __init__(self):
        self.has_apples = False

    # 2)Handle exceptions in below two methods
    def buy_apples(self):
        if self.has_apples:
            raise AppleExistsError("Apples' enough")
        self.has_apples = True

    def finish_apples(self):
        if not self.has_apples:
            raise AppleExistsError("There's no apple")
        self.has_apples = False


# 3)Create the child classes
class ApplePie(AppleRecipe):
    def cook(self):
        print("Make apple pie")


class AppleCake(AppleRecipe):
    def cook(self):
        print("Make apple cake")
