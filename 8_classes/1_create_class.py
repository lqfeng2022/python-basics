# 1)`int` class
number = 6
print(type(number))  # `int` class


# 2)Define a class:
# a)Define a class using `class` keyword, PascalCase name convention
class Apple:
    # b)Define a method inside "Apple" class
    def buy(self):
        print("Buy apples")


# 3)Create an Apple obj
apple = Apple()


# 4)Access Class methods
apple.buy()
print(type(Apple))


# 5)Check if an obj is an instance of a particular class
print(isinstance(apple, Apple))
print(isinstance(apple, int))
