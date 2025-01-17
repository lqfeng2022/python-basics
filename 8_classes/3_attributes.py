class Apple:
    # 2)Class attribute: color
    color = "red"

    # 1)Instance attributes: count, price
    def __init__(self, count, price):
        self.count = count
        self.price = price

    def buy(self):
        print(f"Buy Apple({self.count}, {self.price})")


apple = Apple(1, 3.69)
# 1.2)Set a new instance attribute
apple.origin = "Japan"

apple = Apple(3, 3.69)
apple.buy()


apple = Apple(5, 3.69)
print(apple.color)
# 2.2)Called class attribute using Apple class
print(Apple.color)


# 2.3)Change the class attribute
Apple.color = "green"
print(Apple.color)

apple_two = Apple(2, 0.99)
print(apple_two.color)
