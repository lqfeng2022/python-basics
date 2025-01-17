def calculate_x_factor(phone):
    if phone <= 0:
        # `raise`: To trigger a specific exception
        raise ValueError("Phone number cannot be 0 or less")


try:
    calculate_x_factor(-1)
except ValueError as error:
    print(error)
