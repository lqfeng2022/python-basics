from sys import getsizeof

# 1)A list of 5 items
triples = [x * 3 for x in range(5)]
for x in triples:
    print(x)


# 2)What about a list of 1M items
#  It will store all these 1M numbers in memory
triples = [x * 3 for x in range(1000000)]


# 3)A better approach: `generator` obj
triples = (x * 3 for x in range(1000000))
print(triples)  # triples is a `generator` obj


# 4)`generator` features:
# a)Far more memory-efficient
#  `generator`: 200 bytes (1k or 1M)
triples = (x * 3 for x in range(1000))
print("1k generator size: ", getsizeof(triples))

triples = (x * 3 for x in range(1000000))
print("1M generator size: ", getsizeof(triples))

#  `list`: 8448728 bytes
triples = [x * 3 for x in range(1000000)]
print("1M list size: ", getsizeof(triples))

# b)Cannot get the `generator` length,
#   cus `generator` obj do not store all items in memory
print(len(triples))
