fruits = [("Apple", 9), ("Banana", 6), ("Orange", 16)]


# 1)A regular approach:
# a)Define a function
def sort_fruit(fruit):
    return fruit[1]


# b)Parse sort_fruit to sort() method as a reference
fruits.sort(key=sort_fruit)
print(fruits)


# 2)Lambda function:
#   fromat: key=lambda parameter: expression
fruits.sort(key=lambda fruit: fruit[1])
print(fruits)
