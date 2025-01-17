class Apple:
    # 1)Define a constructor:
    # a)add parameters
    def __init__(self, count, price):
        # b)set attributes
        self.count = count
        self.price = price

    # 3)Pass attributes to buy() method
    def buy(self):
        print(f"Buy Apple({self.count}, {self.price})")


apple = Apple(1, 3.69)

# 2)Access attributes
print(apple.price)

apple.buy()
