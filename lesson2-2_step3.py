from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# берем числа
    num1 = browser.find_element_by_id("num1").text
    x = int(num1)
    num2 = browser.find_element_by_id("num2").text
    y = int(num2)

# ищем правильный вариант
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x+y))    # ищем элемент с текстом "Python"

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
    time.sleep(1)

# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
# закрываем браузер после всех манипуляций
    browser.quit()