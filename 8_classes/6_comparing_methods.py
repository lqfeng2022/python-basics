class Apple:
    def __init__(self, count, price):
        self.count = count
        self.price = price

    # 1)Override __eq__()
    def __eq__(self, other):
        return self.count == other.count and \
            self.price == other.price

    # 2)Override __gt__()
    def __gt__(self, other):
        return self.count > other.count and \
            self.price > other.price


apple = Apple(1, 3.69)
apple_two = Apple(1, 3.69)

print(apple == apple_two)
print(apple > apple_two)
print(apple < apple_two)
