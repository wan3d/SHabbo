import sqlite3
db = sqlite3
connection = db.connect("furnis.db")

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO FURNIS(furni_id, actual_price, low_price)
    VALUES (?, ?, ?)
    """,
    ("","","")
)

# El error de missmatch se debe a que en la base de datos puse que el ID es un INTEGER xd

connection.commit()
connection.close()

