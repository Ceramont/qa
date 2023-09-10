import csv
import sqlite3
import random
from datetime import datetime

now_date = datetime.utcnow().strftime("%H:%M-%d.%m.%Y")

class Operator:
    """Метод для создания таблиц mobile_price, mobile_users"""
    @staticmethod
    def create_table():
        with sqlite3.connect("mobile_calls.db") as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS mobile_price(
                        PriceID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Mts_Mts INTEGER NOT NULL,
                        Mts_Tele2 INTEGER NOT NULL,
                        Mts_Yota INTEGER NOT NULL);""")
            cur.execute("""CREATE TABLE IF NOT EXISTS mobile_users(
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        User TEXT NOT NULL,
                        Balance INTEGER NOT NULL);""")
            print("Создание таблиц mobile_tariff, mobile_users")

    """Метод для первичной вставки данных в mobile_price"""
    @staticmethod
    def insert_mobile_price(data_price):
        with sqlite3.connect("mobile_calls.db") as db:
            cur = db.cursor()
            cur.execute("""INSERT INTO mobile_price (Mts_Mts,Mts_Tele2,Mts_Yota) VALUES (?,?,?)""", data_price)
            print("Таблица mobile_tariff заполнена")

    """Метод для первичной вставки данных в mobile_users"""
    @staticmethod
    def insert_mobile_users(data_users):
        with sqlite3.connect("mobile_calls.db") as db:
            cur = db.cursor()
            cur.execute("""INSERT INTO mobile_users (User,Balance) VALUES (?,?)""", data_users)
            print("Таблица mobile_users заполнена")

    """Метод для обновления данных в mobile_users"""
    @staticmethod
    def update_mobile_users():
        with sqlite3.connect("mobile_calls.db") as db:
            cur = db.cursor()
            cur.execute(f"""UPDATE mobile_users SET Balance = 500 WHERE UserID = 1;""")
            print("Таблица mobile_users обновлена")

    """Основной цикл списания"""
    @staticmethod
    def user_call(user, operator, time):
        with sqlite3.connect("mobile_calls.db") as db:
            cur = db.cursor()
            cur.execute(f"""SELECT Balance
                FROM mobile_users WHERE User = '{user}';""")
            res_balance = cur.fetchone()
            cur.execute(f"""SELECT {operator} From mobile_price;""")
            res_price = cur.fetchone()
            if res_price[0] * time < res_balance[0]:
                cur.execute(f"""UPDATE mobile_users SET Balance = Balance - {res_price[0] * int(time)}""")
                db.commit()
                cur.execute(f"""SELECT Balance FROM mobile_users WHERE UserID = 1""")
                bal_res = cur.fetchone()
                print(f"""Совершен звонок, оператор: {operator}, Цена за минуту: {res_price[0]}, Время: {time}, """
                      f"""Цена звонка: {res_price[0] * time}, Текущий баланс: {bal_res[0]}""")
                Operator.report_operation(now_date, operator, time, res_price[0] * time)
            else:
                cur.execute(f"""SELECT Balance FROM mobile_users WHERE UserID = 1""")
                bal_res = cur.fetchone()
                print(f"""Звонок НЕ СОВЕРШЕН, т.к. недостаточно средств. Цена звонка: {res_price[0] * time}, Текущий баланс: {bal_res[0]}""")

    """Цикл ежедневных звонков"""
    @staticmethod
    def start():
        operator_list = ["Mts_Mts", "Mts_Tele2", "Mts_Yota"]
        for i in range(1, 31):
            Operator.user_call("User1", operator_list[random.randint(0, 2)], random.randint(1, 10))

    @staticmethod
    def report_operation(now_date, operator, count_min, amount):
        user_data = [
             (now_date, operator, count_min, amount)
        ]
        with open("report_mobile.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(
                user_data
            )


op = Operator()
"""Первоначальное создание таблиц и заполнение"""
# op.create_table()
# op.insert_mobile_users(("User1", 500))
# op.insert_mobile_price((1, 2, 3))
# op.report_operation()
"""СТРОКА ДЛЯ ОБНОВЛЕНИЯ БД ДО ПЕРВОНАЧАЛЬНЫХ ЗНАЧЕНИЙ"""
# op.update_mobile_users()
"""ТОЧКА ВХОДА В ПРИЛОЖЕНИЕ"""

op.start()