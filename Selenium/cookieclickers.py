from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
time.sleep(5)
language.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")

cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

while True:

    cookie.click()

    cookies_count_text = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count_text.replace(",", ""))
    
    for i in range(4):
        try:
            product_price_element = driver.find_element(By.ID, product_price_prefix + str(i))
            product_price_text = product_price_element.text.replace(",", "")

            if not product_price_text.isdigit():
                continue

            product_price = int(product_price_text)

            if cookies_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click()
                break
        except Exception as e:
            print(f"Error encountered with product {i}: {e}")
            continue