a = 6
b = 9

# 1)A regular approach
tempt = a
a = b
b = tempt

print('a', a)
print('b', b)


# 2)A Pythonic approach
a, b = b, a

print('a', a)
print('b', b)


# 3)Assign multiple variables one go
c, d = 16, 19
