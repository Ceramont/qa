import sqlite3


class Operator:
    """Метод для создания таблиц mobile_tariff, mobile_users"""
    @staticmethod
    def create_table():
        with sqlite3.connect("mobile.db") as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS mobile_tariff (
                        TariffID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Tariff TEXT NOT NULL,
                        Price INTEGER NOT NULL);""")
            cur.execute("""CREATE TABLE IF NOT EXISTS mobile_users(
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        User_name TEXT NOT NULL,
                        Balance INTEGER NOT NULL,
                        Mobile_tariff_ref INTEGER NOT NULL,
                        Activity TEXT NOT NULL,
                        FOREIGN KEY (Mobile_tariff_ref) REFERENCES mobile_tariff(TariffID)
                        );""")
            print("Создание таблиц mobile_tariff, mobile_users")

    """Метод для первичной вставки данных в mobile_tariff"""
    @staticmethod
    def insert_mobile_tariff(data_tarif):
        with sqlite3.connect("mobile.db") as db:
            cur = db.cursor()
            cur.executemany("""INSERT INTO mobile_tariff (Tariff,Price) VALUES(?,?)""", data_tarif)
            print("Таблица mobile_tariff заполнена")

    """Метод для первичной вставки данных в mobile_users"""
    @staticmethod
    def insert_mobile_users(data_users):
        with sqlite3.connect("mobile.db") as db:
            cur = db.cursor()
            cur.executemany("""INSERT INTO mobile_users (User_name,Balance,Mobile_tariff_ref,Activity) VALUES(?,?,?,
            ?)""", data_users)
            print("Таблица mobile_users заполнена")

    """Метод для обновления данных в mobile_users"""
    @staticmethod
    def update_mobile_users(data_users):
        with sqlite3.connect("mobile.db") as db:
            cur = db.cursor()
            cur.executemany(f"""UPDATE mobile_users SET User_name = ?, Balance = ?, Mobile_tariff_ref = ? , Activity = ? WHERE UserID = ?;""", data_users)
            print("Таблица mobile_users обновлена")

    """Метод для списания денег по тарифу"""
    @staticmethod
    def write_off(user, i):
        with sqlite3.connect("mobile.db") as db:
            cur = db.cursor()
            cur.execute(f"""SELECT Balance, Price, Activity FROM mobile_users
                INNER JOIN mobile_tariff WHERE TariffID = Mobile_tariff_ref AND User_name = '{user}' """)
            res_ex = cur.fetchone()
            if res_ex[0] >= res_ex[1] and res_ex[2] == "Yes":
                cur.execute(f"""UPDATE mobile_users SET Balance = Balance - {int(res_ex[1])} WHERE User_name = "{user}";""")
                db.commit()
                print(f"{i} месяц)Списано у {user}")
            elif res_ex[0] < res_ex[1]:
                if res_ex[2] == "No":
                    print(f"{i} месяц)Пользователь {user} заблокирован")
                else:
                    print(f"{i} месяц)Нельзя списать у {user}, т.к. Недостаточно средств")
                    cur.execute(f"""UPDATE mobile_users SET Activity = "No" WHERE User_name = "{user}";""")
                    db.commit()
    """Основной цикл списания"""
    @staticmethod
    def time_machine(mon_count):
        for i in range(1, mon_count+1):
            Operator.write_off("User1", i)
            Operator.write_off("User2", i)
            Operator.write_off("User3", i)

            """ДЛЯ УДОБСТВА ВОСПРИЯТИЯ"""
            # time.sleep(1)
    """Метод ввода периода расчета"""
    def start(self):
        print("Введите период расчета:")
        c = True
        while c:
            try:
                mon_count = int(input())
                if mon_count <= 0:
                    c = True
                    print("Количество месяцев должно быть больше 0")
                else:
                    c = False
                    self.time_machine(mon_count)
            except ValueError:
                print("Введено недопустимое количество месяцев")
                c = True




op = Operator()
"""Первоначальное создание таблиц и заполнение"""
# op.create_table()
# op.insert_mobile_tariff((("Standart", 500), ("VIP", 1000), ("Premium", 1500)))
# op.insert_mobile_users((("User1", 10000, 2, "Yes"), ("User2", 10000, 3, "Yes"), ("User2", 10000, 3, "Yes")))
"""СТРОКА ДЛЯ ОБНОВЛЕНИЯ БД ДО ПЕРВОНАЧАЛЬНЫХ ЗНАЧЕНИЙ"""
op.update_mobile_users((("User1", 10000, 2, "Yes", 1), ("User2", 10000, 3, "Yes", 2), ("User3", 10000, 1, "Yes", 3)))
"""ТОЧКА ВХОДА В ПРИЛОЖЕНИЕ"""
op.start()