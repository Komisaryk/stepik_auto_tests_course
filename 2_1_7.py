from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    image = browser.find_element_by_id("treasure")
    x = image.get_attribute("valuex")
    answer1 = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(answer1)
    chek_element = browser.find_element_by_class_name("check-input")
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
