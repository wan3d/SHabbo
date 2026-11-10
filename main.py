from furni import Furni

from scrapper import driver
from scrapper import getPrices

from db import cursor

from init_db import storetodatabase

from config import base_endpoint, hotel_parameter

furni_name = "rare_icecream*1" 
# club_sofa
# hween_cloth_r26_possessedpumpkin
# clothing_tattoobody2
# rare_icecream*1
language = "es"

if __name__ == "__main__":
    print("Initializing script...")
    # Entra a la página
    driver.get(base_endpoint + furni_name + hotel_parameter + language)

    actual_price, lowest_price = getPrices(furni_name)
    driver.quit()

    furni = Furni(furni_id=furni_name, actual_price=actual_price, lowest_price=lowest_price, language=language)

    # Inicia la conexión a la base de datos
    storetodatabase(furni)
    

    






