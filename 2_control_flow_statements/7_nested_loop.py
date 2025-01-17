for x in [1, 2, 3]:
    for y in ['b', 'B']:
        print(f"({x}, {y})")


# 1st Iteration:
# [1, 2, 3] ['b', 'B'] (x, y)
#  ^          ^        (1, b)
#                  ^   (1, B)

# 2nd Iteration:
# [1, 2, 3] ['b', 'B']
#     ^       ^        (2, b)
#                  ^   (2, B)

# 3rd Iteration:
# [1, 2, 3] ['b', 'B']
#        ^    ^        (3, b)
#                  ^   (3, B)
