# 1)`try`: Put the implementation statements
try:
    phone = int(input("Phone: "))
# 2)`except`: Catch the exceptions when the try block crushed
#   `as`: define a variable to store the `ValueError` obj,
#         when we print it, we'll get the error message
except ValueError as ex:
    print("You didn't enter a valid phone number")
    print(ex)
    print(type(ex))
# 3)`else`: Will be executed only if no exception is raised in `try` block
else:
    print("No exceptions were thrown")

print("Done")
