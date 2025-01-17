from pathlib import Path
from zipfile import ZipFile

# 1)Working with a ZIP file:
zip = ZipFile("recipes.zip", "w")  # Create a ZIP file
#  Write Data to this zip file
for path in Path("recipe").rglob("*.*"):
    zip.write(path)
zip.close()  # Close this zip file


# 2)Using with statement to create a ZIP file:
with ZipFile("recipes.zip", "w") as zip:
    for path in Path("recipe").rglob("*.*"):
        zip.write(path)


# 3)Reading the info of a ZIP file
with ZipFile("recipes.zip") as zip:
    print(zip.namelist())


# 4)Extracting the ZIP file:
with ZipFile("recipes.zip") as zip:
    zip.extractall("recipes_zip")
