from db import cursor, connection

from furni import Furni

import datetime
current_time = datetime.datetime.now()

def storetodatabase(Furni):
    try:
        cursor.execute(
            """
            INSERT INTO FURNIS(furni_id, actual_price, low_price, last_update)
            VALUES (?, ?, ?, ?)
            """,
            (Furni.furni_id, Furni.actual_price, Furni.lowest_price, current_time)
        )
    except:
            cursor.execute(
            """
            UPDATE FURNIS
            SET actual_price = ?, low_price = ?, last_update = ?
            WHERE furni_id = ?
            """,
            (Furni.actual_price, Furni.lowest_price, current_time, Furni.furni_id)
        )

    connection.commit()
    connection.close()
    cursor.close()