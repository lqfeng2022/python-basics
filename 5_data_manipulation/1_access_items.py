letters = ['a', 'b', 'c', 'd']

# 1)Access a specific item
print(letters[0])
print(letters[-1])

# 2)Modify a specific item
letters[1] = 'B'
print(letters)

# 3)Slice a list then generate a new list
print(letters[0:2])
print(letters[:2])
print(letters[0:])
print(letters[:])


# 4)Slice a list by steps then generate a new list
print(letters[::2])
print(letters[::-1])
