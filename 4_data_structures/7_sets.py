numbers = [1, 2, 6, 6, 9]
print(numbers)

# 1)Define a set
# 1.1)Convert a list to a set
singles = set(numbers)
print(singles)  # a list of unique items, no duplication

# 1.2)Define a set using `{}`, and separate items with `,`
singles = {1, 5}
print(singles)

# 2)Set methods:
# 2.1)Add items to a set
singles.add(9)
print(singles)

# 2.2)Remove existing items from a set
singles.remove(9)
print(singles)

# 2.3)Get the length of a set
print(len(singles))


# 3)Mathematical Operations
first = {1, 2, 3}
second = {1, 6}

# 3.1)union() or `|` operator
print(first | second)
print(first.union(second))

# 3.2)intersection() or `&` operator
print(first & second)
print(first.intersection(second))

# 3.3)difference() or `|` operator
print(first - second)
print(first.difference(second))

# 3.4)symmetric_difference() or `^` operator
print(first ^ second)
print(first.symmetric_difference(second))
