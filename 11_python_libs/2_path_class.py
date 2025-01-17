from pathlib import Path

# 1)Create a Path obj
Path("/usr/local/bin")  # Absolute path
Path()  # Current path
path = Path("recipe/__init__.py")  # Relative path


# 2)Combine paths
Path() / Path("recipe")
Path() / "recipe" / "__init__.py"
Path.home()  # get the home directory


# 3)Path Boolean checking
path.exists()  # check if the file/directory exists
path.is_file()  # check if the path is a file
path.is_dir()   # check if the path is a directory

# 4)Check the specific parts of Path obj
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)


# 5)Useful methods:
#  with_name(): Create a new path obj based on the path obj
new_path = path.with_name("file.txt")
print(new_path)

#  absolute(): Get the absolute path of a file
print(new_path.absolute())

#  with-suffix(): Change the file extension
new_path = path.with_suffix((".txt"))
print(new_path)
