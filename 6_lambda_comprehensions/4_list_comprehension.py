fruits = [("Apple", 9), ("Banana", 6), ("Orange", 16)]

# 1)Map a list:
# a)list(map(lambda func, iterable))
quantity = list(map(lambda fruit: fruit[1], fruits))

# b)[comprehension expression]
quantity = [fruit[1] for fruit in fruits]


# 2)Filter a List
# a)list(filter(lambda func, iterable))
quantity = list(filter(lambda fruit: fruit[1] >= 10, fruits))

# b)[comprehension expression]
quantity = [fruit[1] for fruit in fruits if fruit[1] >= 10]
