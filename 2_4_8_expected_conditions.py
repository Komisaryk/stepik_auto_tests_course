from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) #Функція для обчислення виразу

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    input_value = browser.find_element(By.ID, "input_value")
    x = int(input_value.text)
    answer_value = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(answer_value)

    new_button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    new_button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()