# 1)Global variables: message
message = 'S'

# 4)A better approach:
#   what if you need to define a variable that can be used cross multiple functions?
#   We can define a constant variable using uppercase letters
PI = 3.14


# 2)Local variables: name message
# 2.1_a)name: a function parameter is a local variable
def greet(name):
    # 2.2)message: A local variable, even share the name with a global variable
    message = 'A'


# 3)`global` keyword: A bad practice, AVOID IT!
def greet(name):
    global message
    message = 'A'  # Don't modify a global variable


greet("Melisandre")
print(message)
