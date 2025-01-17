try:
    # When we open a file using the `with` keyword,
    #  this `with` statement ensures the file will be automatically released,
    #  regardless of whether an exception occurs
    with open("app.py") as file:
        print("file opened.")
    phone = int(input("Phone: "))
    x_factor = 100 / phone
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid phone number")
else:
    print("No exceptions were thrown")
