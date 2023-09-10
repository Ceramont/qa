from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
passwd = 'secret_sauce'


"""Функция для поиска элемента со следующими модами:
    0: Простой поиск
    1: Поиск + click()
    2: Поиск + подстановка значений из переменной load
    3: Поиск + извлечение текста внутри элемента """


def f_el(xpath, mode=0, load=''):
    if mode == 0:
        return driver.find_element(By.XPATH, xpath)
    elif mode == 1:
        return driver.find_element(By.XPATH, xpath).click()
    elif mode == 2:
        return driver.find_element(By.XPATH, xpath).send_keys(load)
    elif mode == 3:
        return driver.find_element(By.XPATH, xpath).text


"""Функция авторизации"""


def login(user_name, password):
    f_el("//input[@placeholder='Username']", 2, user_name)
    f_el("//input[@placeholder='Password']", 2, password)
    f_el("//input[@name='login-button']", 1)

"""Точка входа в приложение"""
login(user[0], passwd)

"""Сохранение имен и цен товаров"""
name_pr1 = f_el("//a[@id = 'item_4_title_link']", 3)
print(name_pr1)
price1 = f_el("//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", 3)
print(price1)
name_pr2 = f_el("//*[@id='item_2_title_link']/div", 3)
print(name_pr2)
price2 = f_el("//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", 3)
print(price2)

"""Добавление в корзину 2 товаров"""
f_el("//*[@id='add-to-cart-sauce-labs-onesie']", 1)
f_el("//button[@id= 'add-to-cart-sauce-labs-backpack']", 1)

"""Переход в корзину"""
f_el("//a [@class='shopping_cart_link']", 1)

"""Сохранение имен и цен товаров которые появились в корзине с дальнейшим сравнением их с начальными"""
price1_1 = f_el("//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div", 3)
price2_1 = f_el("//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div", 3)
assert f_el("//a[@id='item_4_title_link']/div", 3) == name_pr1
print(f"Имя {name_pr1} верно" )
assert price1_1 == price1
print(f"Цена на {name_pr1} верна" )
assert f_el("//*[@id='item_2_title_link']/div", 3) == name_pr2
print(f"Имя {name_pr2} верно" )
assert price2_1 == price2
print(f"Цена на {name_pr2} верна" )

"""Переход к заполнению данных получателя"""
f_el("//*[@id='checkout']", 1)
f_el("//*[@id='first-name']", 2, "Alex")
f_el("//*[@id='last-name']", 2, "Sogolovskiy")
f_el("//*[@id='postal-code']", 2, "185030")

"""Переход к результирующей странице с данными о заказе"""
f_el("//*[@id='continue']", 1)
assert f_el("//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div", 3) == price1_1 == price1
print(f"Итоговая цена на {name_pr1} верна" )
assert f_el("//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div", 3) == price2_1 == price2
print(f"Итоговая цена на {name_pr2} верна" )
"""Убираем знак доллара и суммируем значения цен"""
final_expected_summary = float(price1_1[1::]) + float(price2_1[1::])
"""Оставляем только финальную цену и преобразуем в число"""
final_summary = float(f_el("//*[@id='checkout_summary_container']/div/div[2]/div[6]", 3).replace('Item total: $', ''))
assert final_summary == final_expected_summary
print(f"Итоговая сумма без таксы верна: {final_summary}")
tax = round(float(f_el("//*[@id='checkout_summary_container']/div/div[2]/div[7]", 3).replace('Tax: $', ''))
            + final_summary, 2)
final_sum_with_tax = float(f_el("//*[@id='checkout_summary_container']/div/div[2]/div[8]", 3).replace('Total: $', ''))
assert tax == final_sum_with_tax
print(f"Итоговая сумма с таксой верна: {tax}")
driver.close()