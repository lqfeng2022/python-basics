letters = ['a', 'B', 'c']
print(letters)

# 1)Add items to a list
# a)Add a new item to the end of list
letters.append('d')
print(letters)

# b)Add a new item in a particular position
letters.insert(0, '*')
print(letters)


# 2)Remove items from a list
# a)Delete a particular item
letters.remove('B')
print(letters)

# b)Delete a particular item
del letters[0]
print(letters)

# c)Delete a block of items
del letters[0:2]
print(letters)

# d)Delete the whole list
letters.clear()
print(letters)
