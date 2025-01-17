letters = ['a', 'B', 'c']


# 1)Loop over a list using a `for` statement
for letter in letters:
    print(letter)


# 2)What if you want the indexes for each item in a list
# ->enumerate() function
print(enumerate(letters))  # Return an `enumerate` obj

# 2.1)Loop over this `enumerate` obj
for letter in enumerate(letters):
    print(letter)  # Return a tuple in each iteration

# 2.2)Unpack this `enumerate` obj
# A regular approach:
for letter in enumerate(letters):
    print(letter[0], letter[1])

# Using unpacking operation
for index, letter in enumerate(letters):
    print(index, letter)
