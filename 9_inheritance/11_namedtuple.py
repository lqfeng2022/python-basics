from collections import namedtuple

# namedtuple(typename, field_names)
Apple = namedtuple("Apple", ["price", "origin"])

apple_one = Apple(price=3.69, origin="Japan")
apple_two = Apple(price=3.69, origin="Japan")

# 1)Compare two objects
print(apple_one == apple_two)

# Create a new Apple obj taking a new price
apple_one = Apple(price=5.69, origin="French")
print(apple_one.price)
