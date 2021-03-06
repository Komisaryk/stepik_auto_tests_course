from selenium import webdriver
import time
import math
link="http://test1.skillsetz.n2.mavendev.com"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Yuriy")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Komisaryk")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Volyn")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла