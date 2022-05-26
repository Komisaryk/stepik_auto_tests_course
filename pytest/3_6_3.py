import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

links = [
    ("link1","stepik.org/lesson/236895/step/1"),
    ("link2","stepik.org/lesson/236896/step/1"),
    ("link3","stepik.org/lesson/236897/step/1"),
    ("link4","stepik.org/lesson/236898/step/1"),
    ("link5","stepik.org/lesson/236899/step/1"),
    ("link6","stepik.org/lesson/236903/step/1"),
    ("link7","stepik.org/lesson/236904/step/1"),
    ("link8","stepik.org/lesson/236905/step/1"),
]

@pytest.mark.parametrize("linkn, code", links)
def test_link_should_open(browser, linkn, code):
    link = f"http://{code}"
    print(f"Перевірка {linkn}")

    browser.get(link)
    element=browser.find_element(By.CLASS_NAME, "ember-text-area")
    answer = str(math.log(int(time.time())))
    element.send_keys(answer)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    print(message.text)
    assert "Correct" in message.text



