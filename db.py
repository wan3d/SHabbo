import sqlite3

db = sqlite3
connection = db.connect("furnis.db")

cursor = connection.cursor()

cursor.execute(f"""
    INSERT INTO FURNIS(furni_id, actual_price, low_price)
    VALUES (?, ?, ?)
    """,
    ("", "", "")
)

connection.commit()

connection.close()