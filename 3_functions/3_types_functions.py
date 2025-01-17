# 1)Perform a task
def greet(name):
    print(f"Hi {name}")


greet("Hodor")


# 2)Return a value
def greeting(name):
    return f"Hi {name}"


print(greeting("Hodor"))


# Return a `None` obj following "Hi Hodor",
#  cus all functions return `None` by default even they perform tasks
print(greet("Hodor"))
