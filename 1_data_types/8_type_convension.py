# Issue: Cannto concatenate a string to a integer
x = '6'
# y = x + 9  # It'll throw a `TypeError` message
print(type(x))


# Type Converting Methods:
int()  # Convert an obj to an int
float()  # Convert an obj to a float
str()  # Convert an obj to a string
bool()  # Convert an obj to a boolean value


# Fix issue by converting a string to an int
x = '6'
y = int(x) + 9
print(f"{x} + 9: {y}")
