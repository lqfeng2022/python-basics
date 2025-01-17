# ISSUE: price should not be negative
class Apple:
    def __init__(self, price):
        self.price = price


apple = Apple(-3.69)
print(apple.price)


# ------------------------------------------------------------
# SOLUTON 1: Defing getter and setter
class Apple:
    def __init__(self, price):
        # 3)constructor with setter:
        self.set_price(price)

    # 1)getter:
    def get_price(self):
        return self.__price

    # 2)setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


try:
    apple = Apple(-3.69)
    print(apple.get_price())
except ValueError as error:
    print(error)


# ------------------------------------------------------------
# SOLUTION 2: Define a property using property() function
class Apple:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # property(fget, fset, fdel, doc)
    price = property(get_price, set_price)


apple = Apple(3.69)  # Initialize property to 3.69
print(apple.price)  # Access property

try:
    apple = Apple(-3.69)  # Set property to -3.69
    print(apple.price)
except ValueError as error:
    print(error)


# ------------------------------------------------------------
# SOLUTION 3: Using `@property` decorator
class Apple:
    def __init__(self, price):
        # 3)Treat property as a regular attribute
        self.price = price

    # 1)Rename method name, then add `@property` decorator
    @property
    def price(self):
        return self.__price

    # 1)Rename method name, then add `@price.setter` decorator
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


apple = Apple(3.69)  # Initialize property to 3.69
print(apple.price)  # Access property

try:
    apple = Apple(-3.69)
    print(apple.price)
except ValueError as error:
    print(error)


# ------------------------------------------------------------
# Set READ-ONLY property
class Apple:
    def __init__(self, price):
        self.__price = price  # make the property be private

    @property
    def price(self):
        return self.__price

    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError("Price cannot be negative")
    #     self.__price = value


apple = Apple(3.69)
print(apple.price)

apple.price = 5.69
