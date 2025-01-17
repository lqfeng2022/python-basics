class Apple:
    # Magical method: class name is surrounded by __
    def __init__(self, count, price):
        self.count = count
        self.price = price

    # Override __str__():
    def __str__(self):
        return f"({self.count}, {self.price})"

    def buy(self):
        print(f"Buy Apple({self.count}, {self.price})")


apple = Apple(1, 3.69)
print(apple)
