# *args: Pass unkown number of arguments to a function
def display(*numbers):
    print(numbers)


# Return a tuple: a list of values inside `()`, and it's immutable
display(1, 3, 5)


# 1)Iterate a tuple of objs
def display(*numbers):
    for number in numbers:
        print(number)


display(3, 6, 9)


# 2)Iterate then do some calculations
def multiply(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(multiply(3, 6, 9))
