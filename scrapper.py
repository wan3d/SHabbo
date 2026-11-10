# Module that handles the scrapping

# https://securehabbo.com/legacy/{furni_name}?hotel={language}
# This is how the URL is build
from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ap_xpath = "/html/body/div[1]/div/div/div[7]/div/div/dl/div[1]/dd/span[1]"
lp_xpath = "/html/body/div[1]/div/div/div[7]/div/div/section[1]/header/dl/div[1]/dd/span"

driver = webdriver.Chrome()
driver.get(f"https://securehabbo.com/legacy/{furni_name}?hotel={language}")

def getPrices(furni_name: str):
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda driver: 
        driver.find_element(
        By.XPATH, ap_xpath)
        and driver.find_element(
            By.XPATH, lp_xpath))
    
    actual_price = driver.find_element(By.XPATH, ap_xpath)
    low_price = driver.find_element(By.XPATH, lp_xpath)
    return actual_price, low_price


driver.quit()