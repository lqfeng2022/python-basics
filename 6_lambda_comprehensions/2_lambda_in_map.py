fruits = [("Apple", 9), ("Banana", 6), ("Orange", 16)]


# 1)A regular approach:
# a)Define an empty list
quantity = []

# b)Iterate over the fruits list, then add the second item to list in each iteration
for fruit in fruits:
    quantity.append(fruit[1])
print(quantity)


# 2)list(map(lambda func, iterable))
quantity = list(map(lambda fruit: fruit[1], fruits))
print(quantity)
