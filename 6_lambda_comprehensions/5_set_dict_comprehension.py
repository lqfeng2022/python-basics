triples = []

# 1)A regular approach
for x in range(5):
    triples.append(x * 3)
print(triples)


# 2)List comprehension
triples = [x * 3 for x in range(5)]
print(triples)


# 3)Set Comprehension
triples = {x * 3 for x in range(5)}
print(triples)


# 4)Dictionary Comprehension
triples = {x: x * 3 for x in range(5)}
print(triples)


# 5)-> Tuple
triples = (x * 3 for x in range(5))
print(triples)  # We get a `generator` obj
