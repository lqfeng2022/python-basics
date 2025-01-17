class ApplePie():
    def cook(self):
        print("Make apple pie")


class AppleCake():
    def cook(self):
        print("Make apple cake")


# Duck Typing principle:
#  if recipes is an iterable, and recipe has cook() method,
#  cook() function will happy
def cook(recipes):
    for recipe in recipes:
        recipe.cook()


apple_pie = ApplePie()
apple_cake = AppleCake()
cook([apple_pie, apple_cake])
