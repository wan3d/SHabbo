import sqlite3
db = sqlite3
connection = db.connect("furnis.db")

cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS FURNIS(
    furni_id VARCHAR(70) PRIMARY KEY,
    actual_price INTEGER,
    low_price INTEGER,
    last_update TIMESTAMP
    )
"""
)
connection.commit()
connection.close()
