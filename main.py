# Module that handles the scrapping

# https://securehabbo.com/legacy/{furni_name}?hotel={language}
# This is how the URL is build
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


ap_xpath = "/html/body/div[1]/div/div/div[7]/div/div/dl/div[1]/dd/span[1]"
lp_xpath = "/html/body/div[1]/div/div/div[7]/div/div/section[1]/header/dl/div[1]/dd/span"

furni_name = "club_sofa"
language = "es"

# Se rompe cuando le agrego el headless
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome()
driver.get(f"https://securehabbo.com/legacy/{furni_name}?hotel={language}")

def getPrices(furni_name: str):
    wait = WebDriverWait(driver, timeout=5)
    wait.until(lambda driver: 
        driver.find_element(
        By.XPATH, ap_xpath)
        and driver.find_element(
            By.XPATH, lp_xpath))
    
    actual_price = driver.find_element(By.XPATH, ap_xpath)
    low_price = driver.find_element(By.XPATH, lp_xpath)
    return actual_price, low_price


ap, lp = getPrices(furni_name)

import sqlite3
db = sqlite3
connection = db.connect("furnis.db")

cursor = connection.cursor()

import datetime as dt

current_time = dt.datetime.now()

try:
    cursor.execute(
        """
        INSERT INTO FURNIS(furni_id, actual_price, low_price, last_update)
        VALUES (?, ?, ?, ?)
        """,
        (furni_name, int(ap.text), int(lp.text), current_time)
    )
except:
        cursor.execute(
        """
        UPDATE FURNIS
        SET actual_price = ?, low_price = ?, last_update = ?
        WHERE furni_id = ?
        """,
        (int(ap.text), int(lp.text), current_time, furni_name)
    )

connection.commit()
connection.close()

driver.quit()


