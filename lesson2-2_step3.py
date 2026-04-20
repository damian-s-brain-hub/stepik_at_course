from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.ID, "num1")
num_2 = browser.find_element(By.ID, "num2")
x = int(num_1.text)
y = int(num_2.text)
sum = x+y

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()