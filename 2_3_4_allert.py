from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) #Функція для обчислення виразу

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    confirm=browser.switch_to.alert
    confirm.accept()

    x_value = browser.find_element(By.ID, "input_value")
    x = int(x_value.text)

    answer_value=calc(x)

    input=browser.find_element(By.ID, "answer")
    input.send_keys(answer_value)

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()