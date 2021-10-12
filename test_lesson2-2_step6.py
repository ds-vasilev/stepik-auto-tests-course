from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

# скроллим на 100 пикселей вниз
    browser.execute_script("window.scrollBy(0, 100);")

# берем число
    num1 = browser.find_element_by_id("input_value").text
    x = int(num1)
    y = calc(x)

# вносим ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

# код, который заполняет чекбокс и радиобатн
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
    time.sleep(1)

# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
# закрываем браузер после всех манипуляций
    browser.quit()