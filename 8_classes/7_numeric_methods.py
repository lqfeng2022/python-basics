class Apple:
    def __init__(self, count, price):
        self.count = count
        self.price = price

    # Override __add__()
    def __add__(self, other):
        return Apple(self.count + other.count,
                     self.price + other.price)


apple = Apple(10, 3.69)
apple_two = Apple(1, 3.69)

total = apple + apple_two
print(total)
print(total.count)
