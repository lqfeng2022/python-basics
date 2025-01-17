from pathlib import Path
from time import ctime

# 1)Create a Path obj represents a file
path = Path("recipe/__init__.py")

path.exists()  # boolean checking
path.rename("start.txt")  # file renaming
path.unlink()  # file deleting

print(path.stat())  # return file information
print(ctime(path.stat().st_ctime))  # check the file creation time


# 2)Read data from a file
path.read_bytes()
print(path.read_text())

with open("recipe/__init__.py", "r") as file:
    print(file.read())


# 3)Write data to a file
# path.write_bytes()
path.write_text("# TEST")
print(path.read_text())

with path.open("w") as file:
    file.write("# TEST 2")
print(path.read_text())
