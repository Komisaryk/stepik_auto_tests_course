from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) #Функція для обчислення виразу

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_id("input_value") #Шукаємо значення x
    x = int(x_value.text) #Зчитуємо значення х

    answer_value = calc(x) #Обчислюємо вираз маючи хначення х

    answer = browser.find_element_by_id("answer") #Шукаємо поле вводу по айді
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer) #Скролимо знайдене поле вводу вгору вікна браузера

    answer.send_keys(answer_value)  #Вводимо результат обчислень в поле воду

    chek_element = browser.find_element_by_css_selector(".form-check-custom > .form-check-input") #Шукаємо потрібний чекбокс
    chek_element.click() #проставляємо чекбокс

    radio_element = browser.find_element_by_id("robotsRule") #Шукаємо потрібний радіобаттон
    radio_element.click()  #вибираємо радіобатотн

    button = browser.find_element_by_css_selector("[type='submit']") #шукаємо кнопку за типом
    button.click() #клікаєм по кнопці
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()