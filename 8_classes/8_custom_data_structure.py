class FruitKicker:
    # 1)Define a constructor
    #   and set an instance attribute tags to be an empty dict
    def __init__(self):
        self.tags = {}

    # 2)Define an add() method for adding the tags
    def add(self, tag):
        self.tags[tag.lower()] = \
            self.tags.get(tag.lower(), 0) + 1

    # 3)Define a getter for getting the item from tags
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # 4)Define a setter to pass a value to the item of tags
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # 5)Define a method to get the length of our tags
    def __len__(self):
        return len(self.tags)

    # 6)Define a custom method to make this class be an iterable
    def __iter__(self):
        return iter(self.tags)


fruits = FruitKicker()

# Add new tags to our tags  dict
fruits.add("Apple")
fruits.add("apple")
fruits.add("BANANA")
print(fruits.tags)

# Set item value of the tags dict
fruits["apple"] = 6
fruits["banana"] = 9
print(fruits.tags)

# Check the length of fruits obj
print(len(fruits))

# Iterate over our tags dict
for tag in fruits:
    print(tag)
