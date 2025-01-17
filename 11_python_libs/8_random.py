import random
import string

# 1)Generate one random value
print(random.random())
print(random.randint(1, 9))


# 2)Pick one random value
print(random.choice([0, 3, 6, 9]))
print(random.choices([0, 3, 6, 9], k=3))
print(random.choices("abBcdefFg", k=6))


# 3)Generate a random string
print("".join(random.choices("abcdefghi", k=6)))
print(",".join(random.choices("abcdefghi", k=6)))


# 4)Generate a random password
print(string.ascii_letters)
print(string.digits)
print("".join(
    random.choices(
        string.ascii_letters + string.digits, k=6)
))


# 5)Shuffle a list
numbers = [0, 3, 6, 9]
random.shuffle(numbers)
print(numbers)
