# Removing operation on a list queue:
#  when an item is removed from the start of the list,
#  all the subsequent items must shift to the left in memory

# 1)Remove items from a three items queue
# Queue:  [1, 2, 3]
#         [2, 3]
#         [3]


# 2)Remove items from a 1,000 items queue
# ->Performance concern
# Queue:  [1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
#         [2, 3, 4, 5, 6, 7, 8, 9, ...]
#         [3, 4, 5, 6, 7, 8, 9, ...]


# 3)`deque` obj: No performance concerning on large lists
from collections import deque

# Create an empty queue using `deque` Class
musics = deque([])

# Add items to queue
musics.append("Dance With Your Ghost")
musics.append("bad guy")
musics.append("Your Man")
print(musics)

# Remove items from queue
musics.popleft()
print(musics)

# Check the queue is empty or not
if not musics:
    print("empty")
