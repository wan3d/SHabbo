import sqlite3

from furni import Furni

import datetime as dt

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def save_furni(self, furni: Furni):
        with sqlite3.connect(self.db_path) as conn:
            try:
                conn.execute(
                    """
                    INSERT INTO FURNIS(
                    furni_id, 
                    actual_price, 
                    lowest_price, 
                    last_update)
                    VALUES (?, ?, ?, ?)
                    """,
                    (furni.furni_id, furni.actual_price, furni.lowest_price, dt.datetime.now())
                )
            except:
                conn.execute(
                     """
                     UPDATE FURNIS
                     SET actual_price = ?, lowest_price = ?, last_update = ?
                     WHERE furni_id = ?
                     """,
                     (furni.actual_price, furni.lowest_price, dt.datetime.now(), furni.furni_id)
                )
    def create_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS FURNIS (
                furni_id VARCHAR(100) PRIMARY KEY,
                actual_price INTEGER,
                lowest_price INTEGER,
                last_update TIMESTAMP
                )
                """
            )