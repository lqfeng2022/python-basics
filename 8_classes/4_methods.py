class Apple:
    def __init__(self, count, price):
        self.count = count
        self.price = price

    # Define a class-level method
    @classmethod
    def one(cls):
        return cls(1, 3.69)

    # Define an instance method
    def buy(self):
        print(f"Buy Apple({self.count}, {self.price})")


apple = Apple.one()
apple.buy()
