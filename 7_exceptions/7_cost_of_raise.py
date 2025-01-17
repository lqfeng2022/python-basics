from timeit import timeit

# 1)Raising an exception
code_one = """
def calculate_x_factor(phone):
    if phone <= 0:
        raise ValueError("Phone number cannot be 0 or less")

try:
    calculate_x_factor(-1)
except ValueError as error:
    pass # For demo, using `pass` to skip a further processing
"""

# 2)A different approach
code_two = """
def calculate_x_factor(phone):
    if phone <= 0:
        return None

x_factor = calculate_x_factor(-1)
if x_factor == None:
    pass
"""

print(timeit(code_one, number=1000000))  # Output: 0.17
print(timeit(code_two, number=1000000))  # Output: 0.06
