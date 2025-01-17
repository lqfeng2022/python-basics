import sqlite3
import json
from pathlib import Path

# 1)Create a SQLite file:
#  2.1)Load JSON data
recipes = json.loads(Path("recipes.json").read_text())

#  2.2)Connect to SQLite database
with sqlite3.connect("db.sqlite3") as conn:
    # 2.3)Create the Recipes table
    create_table_command = """
    CREATE TABLE IF NOT EXISTS "Recipes" (
        "id" INTEGER,
        "title" TEXT NOT NULL,
        "chef" INTEGER NOT NULL,
        PRIMARY KEY("id")
    );
    """
    conn.execute(create_table_command)

    # 2.4)Create INSERT command,
    insert_command = """
    INSERT INTO Recipes (id, title, chef) VALUES (?, ?, ?)
    """
    # 2.5)then insert data to the table
    for recipe in recipes:
        conn.execute(insert_command, tuple(recipe.values()))
    conn.commit()


# 2)Read the SQLite file
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Recipes"
    cursor = conn.execute(command)

    # Get data in one go
    recipes = cursor.fetchall()
    print(recipes)

    # Iterate over the Cursor obj
    for row in cursor:
        print(row)
