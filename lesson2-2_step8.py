from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Petar")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Petrovich")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("petpet@opet")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "text.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
