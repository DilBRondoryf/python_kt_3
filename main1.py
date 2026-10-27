import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE products SET "
    )

connection.commit()
connection.close()