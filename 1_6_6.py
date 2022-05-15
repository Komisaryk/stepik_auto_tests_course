# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://ars.ua/fasadna-farba-aura-fasad-expo-bila.html")

    # добавляем товар в корзину
    add_button = browser.find_element_by_id("product-addtocart-button")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://ars.ua/fasadna-farba-aura-fasad-residens-bila.html")

    # добавляем товар в корзину
    add_button = browser.find_element_by_id("product-addtocart-button")
    add_button.click()

    # тестовый сценарий
    # открываем корзину
    browser.get("https://ars.ua/checkout")
    time.sleep(10)
    # ищем все добавленные товары
    goods = browser.find_elements_by_css_selector(".opc-wrapper .product-item")

    # проверяем, что количество товаров равно 2

    print(len(goods))
    assert len(goods) == 2
finally:
    time.sleep(30)
    browser.quit()