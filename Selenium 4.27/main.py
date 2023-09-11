import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
passwd = ['secret_sauce']
a = []
"""Словарь с данными о локаторах товаров на 3 страницах (Выбора товара, Корзины, Результата)"""
item_list = {
    '1':
        {'name': 'Sauce Labs Backpack',
         'name_Xpath': "//*[@id='item_4_title_link']/div",
         'cost_Xpath': "//*[@id='item_4_title_link']/../../div[@class='pricebar']/div",
         'add_btn_Xpath': "//*[@id='add-to-cart-sauce-labs-backpack']",
         'cart_name_Xpath': "//*[@id='item_4_title_link']/div",
         'cart_price_Xpath': "//a[@id='item_4_title_link']/../div[@class='item_pricebar']/div",
         'checkout_name_Xpath': "//*[@id='item_4_title_link']/div",
         'checkout_price_Xpath': "//a[@id='item_4_title_link']/../div[@class='item_pricebar']/div"},
    '2': {'name': 'Sauce Labs Bike Light',
          'name_Xpath': "//*[@id='item_0_title_link']/div",
          'cost_Xpath': "//*[@id='item_0_title_link']/../../div[@class='pricebar']/div",
          'add_btn_Xpath': "//*[@id='add-to-cart-sauce-labs-bike-light']",
          'cart_name_Xpath': "//*[@id='item_0_title_link']/div",
          'cart_price_Xpath': "//a[@id='item_0_title_link']/../div[@class='item_pricebar']/div",
          'checkout_name_Xpath': "//*[@id='item_0_title_link']/div",
          'checkout_price_Xpath': "//a[@id='item_0_title_link']/../div[@class='item_pricebar']/div"},
    '3': {'name': 'Sauce Labs Bolt T-Shirt',
          'name_Xpath': "//*[@id='item_1_title_link']/div",
          'cost_Xpath': "//*[@id='item_1_title_link']/../../div[@class='pricebar']/div",
          'add_btn_Xpath': "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
          'cart_name_Xpath': "//*[@id='item_1_title_link']/div",
          'cart_price_Xpath': "//a[@id='item_1_title_link']/../div[@class='item_pricebar']/div",
          'checkout_name_Xpath': "//*[@id='item_1_title_link']/div",
          'checkout_price_Xpath': "//a[@id='item_1_title_link']/../div[@class='item_pricebar']/div"},
    '4': {'name': 'Sauce Labs Fleece Jacket',
          'name_Xpath': "//*[@id='item_5_title_link']/div",
          'cost_Xpath': "//*[@id='item_5_title_link']/../../div[@class='pricebar']/div",
          'add_btn_Xpath': "//*[@id='add-to-cart-sauce-labs-fleece-jacket']",
          'cart_name_Xpath': "//*[@id='item_5_title_link']/div",
          'cart_price_Xpath': "//a[@id='item_5_title_link']/../div[@class='item_pricebar']/div",
          'checkout_name_Xpath': "//*[@id='item_5_title_link']/div",
          'checkout_price_Xpath': "//a[@id='item_5_title_link']/../div[@class='item_pricebar']/div"},
    '5': {'name': 'Sauce Labs Onesie',
          'name_Xpath': "//*[@id='item_2_title_link']/div",
          'cost_Xpath': "//*[@id='item_2_title_link']/../../div[@class='pricebar']/div",
          'add_btn_Xpath': "//*[@id='add-to-cart-sauce-labs-onesie']",
          'cart_name_Xpath': "//*[@id='item_2_title_link']/div",
          'cart_price_Xpath': "//a[@id='item_2_title_link']/../div[@class='item_pricebar']/div",
          'checkout_name_Xpath': "//*[@id='item_2_title_link']/div",
          'checkout_price_Xpath': "//a[@id='item_2_title_link']/../div[@class='item_pricebar']/div"},
    '6': {'name': 'Test.allTheThings() T-Shirt (Red)',
          'name_Xpath': "//*[@id='item_3_title_link']/div",
          'cost_Xpath': "//*[@id='item_3_title_link']/../../div[@class='pricebar']/div",
          'add_btn_Xpath': "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']",
          'cart_name_Xpath': "//*[@id='item_3_title_link']/div",
          'cart_price_Xpath': "//a[@id='item_3_title_link']/../div[@class='item_pricebar']/div",
          'checkout_name_Xpath': "//*[@id='item_3_title_link']/div",
          'checkout_price_Xpath': "//a[@id='item_3_title_link']/../div[@class='item_pricebar']/div"}
}

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


"""Функция для аутентификации пользователя на сайте"""


def login(user_name, password):
    f_el("//input[@placeholder='Username']", 2, user_name)
    f_el("//input[@placeholder='Password']", 2, password)
    f_el("//input[@name='login-button']", 1)


"""Функция для составления строки итогового выбора товаров"""


def choice_string(var):
    res = 'Ваш выбор:'
    for el in var:
        res += f""" {item_list[f'{el}']['name']}; """
    return res


"""Функция выбора товаров"""


def selector(bi=True):
    print("Выберите товары из следующего списка, 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs "
          "Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
    while bi:
        try:
            new = int(input())
            if 0 < new < 7:
                if new not in a:
                    print(f"""Вы выбрали {item_list[f'{new}']['name']}, Для завершения выбора введите 0""")
                    a.append(new)
                else:
                    print("Данный товар уже в списке")
                bi = True
            elif new == 0:
                bi = False
                return a
            else:
                print("Выберете товар под номером от 1 до 6")
                bi = True
        except ValueError:
            print("Неподходящее значение")
            bi = True


"""Функция прохождения бизнес пути"""


def add_to_cart(products_list):
    name_cost_dict = {}
    name_cost_cart_dict = {}
    name_cost_checkout_dict = {}
    temp_dict = {}
    """Создаем словарь с именами и ценами выбранных товаров"""
    for el in products_list:
        temp_dict['name'] = f_el(item_list[f'{el}']['name_Xpath'], 3)
        temp_dict['cost'] = f_el(item_list[f'{el}']['cost_Xpath'], 3)[1::]
        name_cost_dict[f'{el}'] = temp_dict.copy()
        temp_dict.clear()
        f_el(item_list[f'{el}']['add_btn_Xpath'], 1)

    """Переход в корзину"""
    f_el("//a [@class='shopping_cart_link']", 1)

    """Создаем словарь с именами и ценами товаров в корзине"""
    for el in products_list:
        temp_dict['name'] = f_el(item_list[f'{el}']['cart_name_Xpath'], 3)
        temp_dict['cost'] = f_el(item_list[f'{el}']['cart_price_Xpath'], 3)[1::]
        name_cost_cart_dict[f'{el}'] = temp_dict.copy()
        temp_dict.clear()

    """Проверка соответствия выбранных Имен и Цен с Именами и Ценами товаров в корзине"""
    for el in name_cost_dict:
        print(f"Сравниваю имена под номером {el}, {name_cost_dict[el]['name']} и {name_cost_cart_dict[el]['name']}")
        assert name_cost_dict[el]['name'] == name_cost_cart_dict[el]['name']
        print('Имена верны')
        print(f"Сравниваю стоимости под номером {el}, {name_cost_dict[el]['cost']} и {name_cost_cart_dict[el]['cost']}")
        assert name_cost_dict[el]['cost'] == name_cost_cart_dict[el]['cost']
        print('Цены верны')

    """Переход к заполнению данных получателя"""
    f_el("//*[@id='checkout']", 1)
    f_el("//*[@id='first-name']", 2, "Alex")
    f_el("//*[@id='last-name']", 2, "Sogolovskiy")
    f_el("//*[@id='postal-code']", 2, "185030")

    """Переход к результирующей странице с данными о заказе"""
    f_el("//*[@id='continue']", 1)

    """Создаем словарь с именами и ценами товаров на результирующей странице"""
    for el in products_list:
        temp_dict['name'] = f_el(item_list[f'{el}']['cart_name_Xpath'], 3)
        temp_dict['cost'] = f_el(item_list[f'{el}']['cart_price_Xpath'], 3)[1::]
        name_cost_checkout_dict[f'{el}'] = temp_dict.copy()
        temp_dict.clear()

    """Проверка соответствия выбранных Имен и Цен, Имен и Цен товаров в корзине, 
    Имен и Цен товаров на финальной странице """
    for el in name_cost_dict:
        print(f"Сравниваю имена под номером {el}, {name_cost_dict[el]['name']} и "
              f"{name_cost_cart_dict[el]['name']} и {name_cost_checkout_dict[el]['name']}")
        assert name_cost_dict[el]['name'] == name_cost_cart_dict[el]['name'] == name_cost_checkout_dict[el]['name']
        print('Имена верны')
        print(f"Сравниваю стоимости под номером {el}, {name_cost_dict[el]['cost']} и"
              f" {name_cost_cart_dict[el]['cost']} и {name_cost_checkout_dict[el]['cost']}")
        assert name_cost_dict[el]['cost'] == name_cost_cart_dict[el]['cost'] == name_cost_checkout_dict[el]['cost']
        print('Цены верны')

    final_expected_summary = 0.0
    """Считаем стоимость"""
    for el in name_cost_checkout_dict:
        final_expected_summary += float(name_cost_checkout_dict[el]['cost'])

    """Оставляем только финальную цену и преобразуем в число"""
    final_summary = float(
        f_el("//*[@id='checkout_summary_container']/div/div[2]/div[6]", 3).replace('Item total: $', ''))
    print(f"Сравниваю итоговую стоимость и сумму итоговых цен: {final_summary} & {final_expected_summary}")
    assert final_expected_summary == final_summary
    print(f"Итоговая сумма без таксы верна: {final_summary}")
    tax = round(float(f_el("//*[@id='checkout_summary_container']/div/div[2]/div[7]", 3).replace('Tax: $', ''))
                + final_summary, 2)
    final_sum_with_tax = float(
        f_el("//*[@id='checkout_summary_container']/div/div[2]/div[8]", 3).replace('Total: $', ''))
    assert tax == final_sum_with_tax
    print(f"Итоговая сумма с таксой верна: {tax}")


"""Точка входа в приложение"""
b = selector()
print(choice_string(b))
time.sleep(2)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
login(users[0], passwd)
add_to_cart(b)
