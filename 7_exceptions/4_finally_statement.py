try:
    file = open("app.py")
    phone = int(input("Phone: "))
    x_factor = 100 / phone
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid phone number")
else:
    print("No exceptions were thrown")
# When we open a file, don't forget closing it,
#  and you can implement it in a `finally` block.
finally:
    file.close()
