from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from datetime import datetime, date, timedelta

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.get('https://demoqa.com/date-picker')
driver.maximize_window()
# Получаем настоящий день и прибавляем 10 дней
now_date_plus_10 = date.today() + timedelta(10)
input_date = f"""{now_date_plus_10.month}/{now_date_plus_10.day}/{now_date_plus_10.year}"""
date_locator = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# Стираем старую дату костылем
for i in range(10):
    date_locator.send_keys(Keys.BACKSPACE)
# Вводим новую дату
date_locator.send_keys(input_date)
date_locator.send_keys(Keys.RETURN)
