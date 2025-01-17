numbers = [1, 3, 6, 9]

# 1)A regular approach: manually assign each variable one by one
first = numbers[0]
second = numbers[1]
third = numbers[2]
four = numbers[3]


# 2)List unpacking:
# a)Unpack the list into multiple variables in a single operation
first, second, third, four = numbers

# b)Unpack the first two items,
#   then pack the rest into another variable which prefix `*`
first, second, *others = numbers
print(first)
print(others)

# c)Unpack the first and last items,
#   then pack the rest into another variable which prefix `*`
first, *others, last = numbers
print(first, last)
print(others)

# SUMMARY: With this approach, we can pick up the items that you care,
#          then pack the rest into a seperate variable
