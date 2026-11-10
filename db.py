import sqlite3
from config import db_path

db = sqlite3

connection = db.connect(db_path)
cursor = connection.cursor()


