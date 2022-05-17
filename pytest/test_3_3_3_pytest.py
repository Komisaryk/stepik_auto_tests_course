from selenium import webdriver
import time
import pytest


def test_abs1():
        #link = "http://suninjuly.github.io/registration1.html"
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element_by_css_selector(".first_class input[required]")
        First_name.send_keys("Мое имя")
        Last_name = browser.find_element_by_css_selector(".second_class input[required]")
        Last_name.send_keys("Моя фамилия")
        Email = browser.find_element_by_css_selector(".third_class input[required]")
        Email.send_keys("Моя почта")
        time.sleep(10)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Регистрация прошла успешно"

def test_abs2():
        link = "http://suninjuly.github.io/registration1.html"
        #link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element_by_css_selector(".first_class input[required]")
        First_name.send_keys("Мое имя")
        Last_name = browser.find_element_by_css_selector(".second_class input[required]")
        Last_name.send_keys("Моя фамилия")
        Email = browser.find_element_by_css_selector(".third_class input[required]")
        Email.send_keys("Моя почта")
        time.sleep(10)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадаетcd
        # с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Регистрация прошла успешно"

if __name__ == "__main__":
    pytest.main()



