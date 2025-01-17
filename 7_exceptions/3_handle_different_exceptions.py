try:
    phone = int(input("Phone: "))
    x_factor = 100 / phone
# We can put different exceptions inside the `()`,
#  when they share the implementation
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid phone number")
else:
    print("No exceptions were thrown")
