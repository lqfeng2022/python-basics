import sys
from recipe.apple_recipe import chef
# 5)packages: recipe apple_recipe
# 6)sub-package: apple_recipe

# 4)How `import` statement works
print(sys.path)  # It will give us a list of directories

# 8)Get Module informations
print(dir(chef))
print(chef.__name__)  # Return the module names
print(chef.__package__)  # Return the package names
print(chef.__file__)  # Return the file path
