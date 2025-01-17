# 1)Define tuples
# 1.1)Using `()` and separate items with `,`
couple = (6, 9)
print(type(couple))

# 1.2)We can also ommit the `()` to define a tuple
couple = 6, 9
print(type(couple))

# 1.3)Define a single item tuple
couple = 6,
couple = (6,)
couple = (6)
print(type(couple))

# 1.4)Define an empty tuple
couple = ()
print(type(couple))


# 2)Create tuples
# 2.1)Concatenate multiple tuples
couple = (6, 9) + (6,)
print(couple)

# 2.2)Multiply a tuple by an integer
couple = (6, 9) * 2
print(couple)

# 2.3)Convert iterables to tuples
couple = tuple([6, 9])
print(couple)

couple = tuple("hello")
print(couple)


# 3)Tuple Operations
couple = (1, 6, 9)

# 3.1)Access a specific item
print(couple[0])

# 3.2)Slice a block of items
print(couple[0:3])

# 3.3)Unpack a tuple
x, y, z = couple
print(z)

# 3.4)Check if an item exists or not
if 8 in couple:
    print("exists")

# 3.5)Iterate over a tuple
for a in couple:
    print(a)

# 3.6)Tuple is immutable
couple[0] = 8
