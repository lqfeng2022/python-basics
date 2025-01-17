letters = ['a', 'B', 'c']
print(letters)

# 1)Find a particular item
print(letters.index('a'))

# 2)Find a particular item using `if` statement
if 'b' in letters:
    print(letters.index('b'))

# 3)Count the number of a particular item
print(letters.count('b'))
print(letters.count('B'))
