from pathlib import Path

# 1)Create a Path obj represents a directory
path = Path("recipe")

path.mkdir()  # create a new directory
path.rename("recipe_master")  # rename the existing path
path.rmdir()  # remove the existing path


# 2)iterdir() -> map object
print(path.iterdir())
for p in path.iterdir():
    print(p)

#  List comprehension
paths = [p for p in path.iterdir()]
print(paths)

#  List comprehension with a filter
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)


# 3)Global Searching:
paths = [p for p in path.glob("*.py")]
print(paths)

#  Recursive global Searching:
py_files = [p for p in path.glob("**/*.py")]
py_files = [p for p in path.rglob("*.py")]
print(py_files)
