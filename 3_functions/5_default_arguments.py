# Default Argument: by=1
# 3)We cannot put a required parameter after this optional one
def increment(number, by=1):
    return number + by


# 1)We can skip the 2nd argument
print(increment(2))  # Output: 3

# 2)We can do provide the 2nd argument, and it will override the default
print(increment(2, 7))  # Output: 9
