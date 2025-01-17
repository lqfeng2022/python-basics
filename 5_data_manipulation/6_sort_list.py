numbers = [1, 69, 13, 9, 8]
print(numbers)

# 1)sort() method
# a)Generate a new ascending order List
numbers.sort()
print(numbers)

# b)Generate a new descending order List
numbers.sort(reverse=True)
print(numbers)


# 2)sorted() function
print(sorted(numbers))
print(numbers)

print(sorted(numbers, reverse=True))
print(numbers)


# 3)Sort a list of tuples
fruits = [("Apple", 9), ("Banana", 6), ("Orange", 16)]


# a)Define a sorting function
def sort_fruit(fruit):
    return fruit[1]


# b)Pass the sort_fruit to sort() method as a reference,
#   and don't forget specifying the `key` argument
fruits.sort(key=sort_fruit)
print(fruits)
