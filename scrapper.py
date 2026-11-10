# https://securehabbo.com/legacy/{furni_name}?hotel={language}
# This is how the URL is build
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import ap_xpath, lp_xpath, timeout

# Se rompe cuando le agrego el headless
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome()

def getPrices(furni_name: str):
    wait = WebDriverWait(driver, timeout)
    wait.until(lambda driver: 
        driver.find_element(
        By.XPATH, ap_xpath)
        and driver.find_element(
            By.XPATH, lp_xpath))
    
    actual_price = driver.find_element(By.XPATH, ap_xpath).text
    low_price = driver.find_element(By.XPATH, lp_xpath).text
    return int(actual_price), int(low_price)

