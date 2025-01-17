# 1)Import `array` class from a `array` module
from array import array


# 2)Create an integer array using `array` Class
# 'i': data type, means integer
numbers = array('i', [1, 2, 3])
print(numbers)


# 3)Add items to our array
# 3.1)Add a new item to the end
numbers.append(6)
print(numbers)

# 3.2)Add a new item to a particular position
numbers.insert(1, 9)
print(numbers)


# 4)Remove items from our array
# 4.1)Pop the last item
numbers.pop()
print(numbers)

# 4.2)Delete a particular item
numbers.remove(9)
print(numbers)


# 5)Cannot set a float number to our array, cus it's typed as integer
numbers[0] = 0.69
