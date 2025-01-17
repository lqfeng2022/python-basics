fruits = [("Apple", 9), ("Banana", 6), ("Orange", 16)]

# 1)A regular approach:
# a)Define an empty list
filters = []

# b)Iterate over the fruits list,
#   then add the second item to list in each iteration when it met a specific condition
for fruit in fruits:
    if fruit[1] >= 10:
        filters.append(fruit)
print(filters)


# 2)list(filter(lambda func, iterable))
filters = list(filter(lambda fruit: fruit[1] >= 10, fruits))
print(filters)
