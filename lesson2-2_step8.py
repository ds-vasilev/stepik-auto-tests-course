from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
#открываем браузер
    browser = webdriver.Chrome()
    browser.get(link)

#приатаченье файла
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

#забиваем данные с помощью поиска элементов
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input4 = browser.find_element_by_name("email")
    input4.send_keys("email@email.em")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

