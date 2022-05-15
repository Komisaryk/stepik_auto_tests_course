from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1")
    a = int(number1.text)
    number2 = browser.find_element_by_id("num2")
    b = int(number2.text)
    answer=str(a+b)
    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(answer)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


