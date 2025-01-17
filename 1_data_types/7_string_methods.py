greet = "Hello Python"

# Get the string length
print(len(greet))
# Covert the string to uppercase
print(greet.upper())
# Covert the string to lowercase
print(greet.lower())
# Capitalize the first letter of each word in a string
print(greet.title())


greet = "  Hello Python"
# Strip strings
print(greet.strip())
print(greet.lstrip())


greet = "Hello Python"
# Find the characters
print(greet.find("Hel"))
print(greet.find("E"))


greet = "Hello Python"
# Replace the characters
print(greet.replace("Python", "Jon Snow"))
