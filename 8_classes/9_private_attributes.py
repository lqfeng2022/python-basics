class FruitKicker:
    def __init__(self):
        # 1)tags -> __tags: make it be private
        self.__tags = {}

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count


fruits = FruitKicker()

# 2)Issue: we can still get accessing it like this:
print(fruits.__dict__)
print(fruits._FruitKicker__tags)
