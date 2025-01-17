# **user: Pass unkown number of keyword arguments
def save_user(**user):
    print(user)


# Return a dictionary: a list of key-value pairs inside `{}`
save_user(id=1, name="Jon", age=22)


# **user: consider it as a dictionary
def save_user(**user):
    print(user["id"])
    print(user["name"])


save_user(id=1, name="Jon", age=22)
