import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        in_stock INTEGER DEFAULT 1
    )  
""") 

# cursor.execute("INSERT INTO products (name, price ) VALUES ('Товар 1', 500)") 
# cursor.execute("INSERT INTO products (name, price ) VALUES (?, ?)",  ('Товар 888', 1213310)) 
# cursor.executemany(
#     "INSERT INTO products (name, price ) VALUES (?, ?)",
#     [
#         ("Товар мой", 500000),
#         ("Товар eee", 50000),
#         ("Товар ppp", 5000)        
#     ]
#     )
cursor.execute("SELECT * FROM products WHERE price > 5000 ORDER BY price DESC")
for row in cursor:
    print(row)

print("")

cursor.execute("SELECT * FROM products ORDER BY price ASC LIMIT 2")
for row in cursor:
    print(row)

print("")

cursor.execute("SELECT * FROM products WHERE name LIKE 'Т%' ")
for row in cursor:
    print(row)
    
cursor.execute("DELETE FROM products")


connection.commit()
connection.close()