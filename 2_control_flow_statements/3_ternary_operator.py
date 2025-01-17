age = 20

# 1)if/else statments
if age >= 18:
    message = "Legal age"
else:
    message = "Underage"

print(message)


# 2)Ternary operator: a cleaner way to write if/else statement
message = "Legal age" if age >= 18 else "Underage"
print(message)
