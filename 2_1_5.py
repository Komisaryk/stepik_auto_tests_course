from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)
    chek_element = browser.find_element_by_class_name("form-check-input")
    chek_element.click()
    radio_element = browser.find_element_by_css_selector("[value='robots']")
    radio_element.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()