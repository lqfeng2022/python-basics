first_name = "Jon"
last_name = "Snow"

# Concatenate strings
full_name = first_name + " " + last_name
print(full_name)


# f-strings: an elegent way to format strings
full_name = f"{first_name} {last_name}"
print(full_name)


# We can add expression inside the f-strings
new_string = f"{first_name} {last_name}, you know {9 - 9}"
print(new_string)
