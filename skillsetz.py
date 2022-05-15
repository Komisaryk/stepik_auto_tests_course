from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://client:password123@test1.skillsetz.n2.mavendev.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    button_login = browser.find_element(By.CLASS_NAME, "icon-skillz-login")
    button_login.click()
    button_get_started = browser.find_element(By.CLASS_NAME, "get-started")
    button_get_started.click()
    button_choose_buying = browser.find_element(By.CSS_SELECTOR, "[for='buying']")
    button_choose_buying.click()
    button_choose_individual = browser.find_element(By.CSS_SELECTOR, "[data-account-type='personal_account']")
    button_choose_individual.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()