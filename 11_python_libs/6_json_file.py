import json
from pathlib import Path


# 1)Create a list of dictionaries
recipes = [
    {"id": 1, "title": "Apple Pie", "chef": "Jamie"},
    {"id": 2, "title": "Apple Cake", "chef": "Helena"},
]

# 2)Create a JSON file called data
data = json.dumps(recipes)
print(data)


# 3)Read the JSON file
data = Path("recipes.json").read_text()
recipes = json.loads(data)

print(recipes)
print(recipes[0])
print(recipes[0]["title"])
