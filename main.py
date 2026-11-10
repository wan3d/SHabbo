from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from init import Furni


# https://securehabbo.com/legacy/{furni_name}?hotel={language}

driver = webdriver.Chrome()

furni_name = "bc_gift_31days"
language = "es"

driver.get(f"https://securehabbo.com/legacy/{furni_name}?hotel={language}")
wait = WebDriverWait(driver, timeout=2)

wait.until(lambda driver: 
    driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[7]/div/div/dl/div[1]/dd/span[1]")
    and driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div[7]/div/div/section[1]/header/dl/div[1]/dd/span"))

actual_price = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[7]/div/div/dl/div[1]/dd/span[1]").text
low_price = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[7]/div/div/section[1]/header/dl/div[1]/dd/span").text


furni = Furni(furni_name, int(actual_price), int(low_price))

import sqlite3
db = sqlite3
connection = db.connect("furnis.db")

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO FURNIS(furni_id, actual_price, low_price)
    VALUES (?, ?, ?)
    """,
    (int(furni.furni_id), int(furni.actual_price), int(furni.low_price))
)

# El error de missmatch se debe a que en la base de datos puse que el ID es un INTEGER xd


connection.commit()

connection.close()

driver.quit()       