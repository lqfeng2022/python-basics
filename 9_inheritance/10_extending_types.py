# 1)Extend the `str` class
class Triple(str):
    def triplicate(self):
        return self * 3


emoji = Triple("lol_")

print(emoji.upper())
print(emoji.triplicate())


# 2)Extend the `list` Class
class SimpleList(list):
    def append(self, object):
        print("append method called")
        super().append(object)


list = SimpleList()
list.append('b')

print(list)
