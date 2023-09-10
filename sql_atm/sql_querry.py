import csv
import datetime
import sqlite3

now_data = datetime.datetime.utcnow().strftime("%H:%M-%d.%m.%Y")


class SQL_atm:
    @staticmethod
    def create_table():
        with sqlite3.connect("atm.db") as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Users_data(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            Number_card INTEGER NOT NULL,
            Pin_code INTEGER NOT NULL,
            Balance INTEGER NOT NULL);""")
            print("Создание таблицы Users_data")

    @staticmethod
    def insert_users(data_users):
        with sqlite3.connect("atm.db") as db:
            cur = db.cursor()
            cur.execute("""INSERT INTO Users_data (Number_card,Pin_code,Balance) VALUES(?,?,?)""", data_users)
            print("Создание нового пользователя")

    @staticmethod
    def input_card(number_card):
        try:
            with sqlite3.connect("atm.db") as db:
                cur = db.cursor()
                cur.execute(f"""SELECT Number_card From Users_data WHERE Number_card = {number_card}""")
                res_card = cur.fetchone()
                if res_card is None:
                    print("\033[31m{}".format("Введен неверный номер карты"))
                    print("\033[0m")
                    return False
                else:
                    print("\033[32m{}".format(f"Введен верный номер карты: {number_card}"))
                    print("\033[0m")
                    return True
        except :
            print("\033[31m{}".format("Введеный номер карты имеет неверный формат"))
            print("\033[0m")
            return False

    @staticmethod
    def input_code(number_card):
        pin_code = input("Введите pincode:")
        try:
            with sqlite3.connect("atm.db") as db:
                cur = db.cursor()
                cur.execute(f"""SELECT Pin_code From Users_data WHERE Number_card = {number_card}""")
                res_code = cur.fetchone()
                input_pin = res_code[0]
                if input_pin == int(pin_code):
                    print("\033[32m{}".format("Введен верный пинкод"))
                    print("\033[0m")
                    return True
                else:
                    print("\033[31m{}".format("Введен неверный пинкод"))
                    print("\033[0m")
                    return False
        except ValueError:
            print("\033[31m{}".format("Введен неизвестный пин код"))
            print("\033[0m")

    @staticmethod
    def info_balance(number_card):
        with sqlite3.connect("atm.db") as db:
            cur = db.cursor()
            cur.execute(f"""SELECT Balance From Users_data WHERE Number_card = {number_card}""")
            result_info_balance = cur.fetchone()
            balance_card = result_info_balance[0]
            print(f"Баланс карты: {balance_card}")

    @staticmethod
    def withdraw_money(number_card):
        amount = input("Введите сумму которую хотите получить")
        with sqlite3.connect("atm.db") as db:
            cur = db.cursor()
            try:
                cur.execute(f"""SELECT Balance From Users_data WHERE Number_card = {number_card}""")
                result_info_balance = cur.fetchone()
                balance_card = result_info_balance[0]
            except:
                print("Недопустимый номер карты")
            try:
                if int(amount) > balance_card:
                    print("Недостаточно средств")
                    return False
                else:
                    cur.execute(f"""UPDATE Users_data SET Balance = Balance - {amount} WHERE Number_card = {number_card};""")
                    db.commit()
                    SQL_atm.info_balance(number_card)
                    return True
            except:
                print("Попытка выполнить неккоректное действие")
                return False

    @staticmethod
    def deposit_money(number_card):
        amount = input("Введите сумму которую хотите внести")
        with sqlite3.connect("atm.db") as db:
            cur = db.cursor()
            try:
                cur.execute(f"""UPDATE Users_data SET Balance = Balance + {amount} WHERE Number_card = {number_card};""")
                db.commit()
                SQL_atm.info_balance(number_card)
                SQL_atm.report_operation_1(now_data, number_card, "2", amount, "")
                return True
            except:
                print("Попытка выполнить неккоректное действие")
                return False
    """Метод перевода денег с карты на карту"""
    @staticmethod
    def transfer_money(number_card):
        try:
            number_transfer_card = int(input("Введите номер карты на которую вы хотите перевести\n"))
        except:
            print("\033[31m{}".format("Недопустимый номер карты"))
            print("\033[0m")
            return False

        if int(number_transfer_card) == int(number_card):
            print("\033[31m{}".format("Вы не можете перевести средства на ту же карту"))
            print("\033[0m")
            return False
        else:
            with sqlite3.connect("atm.db") as db:
                cur = db.cursor()
                cur.execute(f"""SELECT Number_card From Users_data WHERE Number_card = {number_transfer_card}""")
                res_tr_card = cur.fetchone()
                if res_tr_card is not None:
                    amount = input("Введите сумму которую хотите перевести\n")
                    cur.execute(f"""SELECT Balance From Users_data WHERE Number_card = {number_card}""")
                    result_info_balance = cur.fetchone()
                    balance_card = result_info_balance[0]
                    try:
                        if int(amount) > balance_card:
                            print("\033[31m{}".format("Недостаточно средств"))
                            print("\033[0m")
                            return False
                        elif int(amount) <= 0:
                            print("\033[31m{}".format("Сумма должна быть больше 0"))
                            print("\033[0m")
                            return False
                        else:
                            cur.execute(
                                f"""UPDATE Users_data SET Balance = Balance - {amount} WHERE Number_card = {number_card};""")
                            cur.execute(
                                f"""UPDATE Users_data SET Balance = Balance + {amount} WHERE Number_card = {number_transfer_card};""")
                            db.commit()
                            SQL_atm.info_balance(number_card)
                            SQL_atm.report_operation_1(now_data, number_card, "3", amount, number_transfer_card)
                            SQL_atm.report_operation_2(now_data, number_transfer_card, "3", amount, number_card)
                            print("\033[32m{}".format("Операция успешно выполнена"))
                            print("\033[0m")
                            return True
                    except:
                        print("\033[31m{}".format("Попытка выполнить неккоректное действие"))
                        print("\033[0m")
                        return False
                else:
                    print("\033[31m{}".format("Данной карты не существует"))
                    print("\033[0m")
                    return False


    @staticmethod
    def input_operation(number_card):
        while True:
            operation = input(
                """Введите нужное действие \n 1. Узнать баланс\n 2. Снять средства\n 3. Положить средства\n 4. Выйти\n 5. Перевести средства\n""")
            if operation == "1":
                SQL_atm.info_balance(number_card)
            elif operation == "2":
                SQL_atm.withdraw_money(number_card)
            elif operation == "3":
                SQL_atm.deposit_money(number_card)
            elif operation == "4":
                print("Завершение работы")
                return False
            elif operation == "5":
                SQL_atm.transfer_money(number_card)
            else:
                print("Операция недоступна")

    @staticmethod
    #
    def report_operation_1(now_date, number_card, type_operation, amount, payee):
        user_data = [
            (now_date, number_card, type_operation, amount, payee)
        ]
        with open("report_1.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(
                user_data
            )

    @staticmethod
    def report_operation_2(date, payee, type_operation, amount, sender):
        user_data = [
            # ("Date", "Payee", "type_operation", "amount", "Sender")
            (date, payee, type_operation, amount, sender)
        ]
        with open("report_2.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(
                user_data
            )
