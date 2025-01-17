# 1)Define a dictionary
# 1.1){key: value}
drama = {"Rose": 6, "Smith": 9}
print(drama)

# 1.2)dict(key=value)
drama = dict(Rose=6, Smith=9)
print(drama)


# 2)Dictionary Operations
# 2.1)Access a dictionary value with its key
print(drama["Rose"])

# 2.2)Modify a dictionary
drama["Rose"] = 9
print(drama)

# 2.3)Add a new value
drama["Fiona"] = 8
print(drama)


# 3)Accessing Issue:
#   try to access a key that doesn’t exist in the dict

# 3.1)Access a key using if statement
if "Jack" in drama:
    print(drama["Jack"])

# 3.2)Use get() method: a better approach
print(drama.get("Jack"))  # Output: None
print(drama.get("Jack", 0))  # If the key is not found, return 0


# 4)Delete items
drama = dict(Rose=6, Smith=9, Fiona=6)
print(drama)

del drama["Rose"]
print(drama)


# 5)Loop over a dict
drama = dict(Rose=6, Smith=9)

for x in drama:
    print(x, drama[x])

for x in drama.items():
    print(x)  # We'll get a tuple in each iteration


# 6)Unpack a dict
drama = dict(Rose=6, Smith=9)

for key, value in drama.items():
    print(key, value)
