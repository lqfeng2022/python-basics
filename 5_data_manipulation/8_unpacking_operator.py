# 1)EXAMPLE ONE:
numbers = [1, 6, 9]

print(1, 6, 9)
print(numbers)

# `*` operator: Unpack an iterable except the dictionary
print(*numbers)


# 2)EXAMPLE TWO:
# a)We can unpack a string or `range` obj as well
# b)Unpack multiple iterables then put them into a list
values = [*range(3), *"Hello"]
print(values)


# 3)EXAMPLE THREE:
first = [6, 9]
second = [6]

values = [*first, 'b', *second, *"Hello"]
print(values)


# 4)EXAMPLE FOUR:
first = {'b': 6}
second = {'b': 66, 'B': 9}

# `**` operator: Unpack a dictionary
values = {**first, **second, 'd': 8}
print(values)
