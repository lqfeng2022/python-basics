# 1)Define a list:
#   Using `[]` and seperate items with `,`
letters = ['a', 'b', 'c']  # A list of strings
numbers = [1, 2, 3, 4, 5]  # A list of numbers
booleans = [True, False, True]  # A list of booleans
lists = ['a', 6, True, 9]  # A list of any type values

# A list of lists (matrix/2-dimension list)
matrix = [[0, 1], [2, 3]]


# 2)Multiply a list
zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros = [0] * 9
print(zeros)


# 3)Concatenate multiple lists using `+` operator
combined = zeros + letters
print(combined)


# 4)Convert an iterable to a list
# 4.1)Convert a `range` obj to a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers = list(range(9))

# 4.2)Convert a string to a list
chars = list("Hello 2025")
print(chars)
