import sqlite3 as sql

# Функция обмена
def exchange(ex_list):
    # Запрос с получением баланса
    cur.execute("""SELECT * FROM users_balance""")
    # sq_list[1] -Баланс в рублях, sq_list[2] -Баланс В Долларах, sq_list[3] - Баланс в Евро,
    sq_list = cur.fetchone()
    # Если Отдаем Рубли
    if ex_list[2] == 'RUB':
        # Если получаем доллары
        if ex_list[0] == 'USD':
            # Проверка достаточно ли средств на балансе
            if int(ex_list[1])*70 <= int(sq_list[1]):
                # Присвоение новых значений для получения долларов в обмен на рубли
                new_rub = round((sq_list[1]) - (ex_list[1])*70, 2)
                new_usd = int(sq_list[2]) + int(ex_list[1])
                cur.execute(f"UPDATE users_balance SET Balance_RUB = {new_rub},Balance_USD = {new_usd} ")
                db.commit()
                print('Обмен успешно выполнен')
                cur.execute("""SELECT * FROM users_balance""")
                sq_list = cur.fetchone()
                print(f"Ваш текущий баланс: {sq_list[1]} Рублей,{sq_list[2]} Долларов,{sq_list[3]} Евро ")
            else:
                print("Недостаточно средств")
                selector()
        # Если получаем ЕВРО
        elif ex_list[0] == 'EUR':
            if int(ex_list[1]) * 80 <= int(sq_list[1]):
                new_rub = round((sq_list[1]) - (ex_list[1]) * 80, 2)
                new_eur = int(sq_list[3]) + int(ex_list[1])
                cur.execute(f"UPDATE users_balance SET Balance_RUB = {new_rub},Balance_EUR = {new_eur} ")
                db.commit()
                print('Обмен успешно выполнен')
                cur.execute("""SELECT * FROM users_balance""")
                sq_list = cur.fetchone()
                print(f"Ваш текущий баланс: {sq_list[1]} Рублей,{sq_list[2]} Долларов,{sq_list[3]} Евро ")
            else:
                print("Недостаточно средств")
                selector()
    # Если отдаем Доллары
    elif ex_list[2] == 'USD':
        # Если получаем Рубли
        if ex_list[0] == 'RUB':
            if int(ex_list[1])/70 <= int(sq_list[2]):
                new_usd = round((sq_list[2]) - (ex_list[1])/70, 2)
                new_rub = int(sq_list[1]) + int(ex_list[1])
                cur.execute(f"UPDATE users_balance SET Balance_RUB = {new_rub},Balance_USD = {new_usd} ")
                db.commit()
                print('Обмен успешно выполнен')
                cur.execute("""SELECT * FROM users_balance""")
                sq_list = cur.fetchone()
                print(f"Ваш текущий баланс: {sq_list[1]} Рублей,{sq_list[2]} Долларов,{sq_list[3]} Евро ")
            else:
                print("Недостаточно средств")
                selector()
        # Если получаем ЕВРО
        elif ex_list[0] == 'EUR':
            if int(ex_list[1]) * 1.15 <= int(sq_list[2]):
                new_usd = round((sq_list[2]) - (ex_list[1]) * 1.15, 2)
                new_eur = round(int(sq_list[3]) + int(ex_list[1]))
                cur.execute(f"UPDATE users_balance SET Balance_USD = {new_usd},Balance_EUR = {new_eur} ")
                db.commit()
                print('Обмен успешно выполнен')
                cur.execute("""SELECT * FROM users_balance""")
                sq_list = cur.fetchone()
                print(f"Ваш текущий баланс: {sq_list[1]} Рублей,{sq_list[2]} Долларов,{sq_list[3]} Евро ")
            else:
                print("Недостаточно средств")
                selector()
    # Если отдаем ЕВРО
    elif ex_list[2] == 'EUR':
        print("123")
        # Если получаем Рубли
        if ex_list[0] == 'RUB':
            if int(ex_list[1]) / 80 <= int(sq_list[3]):
                new_eur = round((sq_list[3]) - (ex_list[1]) / 80, 2)
                new_rub = int(sq_list[1]) + int(ex_list[1])
                cur.execute(f"UPDATE users_balance SET Balance_RUB = {new_rub},Balance_EUR = {new_eur} ")
                db.commit()
                print('Обмен успешно выполнен')
                cur.execute("""SELECT * FROM users_balance""")
                sq_list = cur.fetchone()
                print(f"Ваш текущий баланс: {sq_list[1]} Рублей,{sq_list[2]} Долларов,{sq_list[3]} Евро ")
            else:
                print("Недостаточно средств")
                selector()
        # Если получаем Доллары
        if ex_list[0] == 'USD':
            if int(ex_list[1]) * 0.87 <= int(sq_list[3]):
                new_eur = round((sq_list[3]) - (ex_list[1]) * 0.87, 2)
                new_usd = round(int(sq_list[2]) + int(ex_list[1]))
                cur.execute(f"UPDATE users_balance SET Balance_USD = {new_usd},Balance_EUR = {new_eur} ")
                db.commit()
                print('Обмен успешно выполнен')
                cur.execute("""SELECT * FROM users_balance""")
                sq_list = cur.fetchone()
                print(f"Ваш текущий баланс: {sq_list[1]} Рублей,{sq_list[2]} Долларов,{sq_list[3]} Евро ")
            else:
                print("Недостаточно средств")
                selector()
    selector()

# Функция выбора валют для обмена
def selector():
    ex_list = []
    print("Введите какую валюту вы желаете получить:\n 1. RUB \n 2. USD \n 3. EUR")
    try:
        curr_to_recieve = int(input())
    except ValueError:
        curr_to_recieve = -1

    while curr_to_recieve != 1 and curr_to_recieve != 2 and curr_to_recieve != 3:
        print("Необходимо ввести либо 1, либо 2, либо 3")
        try:
            curr_to_recieve = int(input())
        except ValueError:
            curr_to_recieve = -1

    if curr_to_recieve == 1:
        ex_list.append("RUB")
    elif curr_to_recieve == 2:
        ex_list.append("USD")
    elif curr_to_recieve == 3:
        ex_list.append("EUR")

    print("Какая сумма Вас интересует?")
    try:
        amount = float(input())
    except ValueError:
        amount = -1
    str_am = str(amount)
    while len(str(amount)) == 0 or amount <= 0 or len(str_am[str_am.index(".")+1:]) > 2:
        print("Вы ввели неподходящую сумму (Сумма должна быть > 0, а также иметь не более 2 знаков после запятой)")
        try:
            amount = float(input())
        except ValueError:
            amount = -1
        str_am = str(amount)
    ex_list.append(amount)
    print("Какую валюту готовы предложить взамен?\n 1. RUB\n 2. USD\n 3. EUR")
    try:
        curr_to_give = int(input())
    except ValueError:
        curr_to_give = -1

    while curr_to_give != 1 and curr_to_give != 2 and curr_to_give != 3 or curr_to_give == curr_to_recieve:
        if curr_to_give == curr_to_recieve:
            print("Нельзя поменять одинаковую валюту")
        else:
            print("Необходимо ввести либо 1, либо 2, либо 3")
        try:
            curr_to_give = int(input())
        except ValueError:
            curr_to_give = -1
    #Вызов выбранной функции
    if curr_to_give == 1:
        ex_list.append("RUB")
    elif curr_to_give == 2:
        ex_list.append("USD")
    elif curr_to_give == 3:
        ex_list.append("EUR")
    # ex_list[0] - что получаем, ex_list[1] - сколько, ex_list[2] - что отдаем
    exchange(ex_list)

# Точка входа в приложение
# Подключение к бд
try:
    db = sql.connect('exchanger.db')
    cur = db.cursor()
    print("Подключение к бд выполнено")
except Exception:
    print("Подключение к бд не выполнено")

"""Первичное создание таблицы с добавлением 1 строки """
# user_data_param = (100000, 1000, 1000)
# cur.execute("""CREATE TABLE IF NOT EXISTS users_balance(
# UserID INTEGER PRIMARY KEY AUTOINCREMENT,
# Balance_RUB FLOAT NOT NULL,
# Balance_USD FLOAT NOT NULL,
# Balance_EUR INTEGER NOT NULL);""")
#
# cur.execute("""INSERT INTO users_balance(Balance_RUB,Balance_USD,Balance_EUR)
# VALUES (?,?,?)""", user_data_param)
# db.commit()
print("Добро пожаловать в наш обменный пункт, курс валют следующий:\n 1 USD = 70 RUB\n 1 EUR = 80 RUB\n 1 USD = 0,87 EUR"
      " \n 1 EUR = 1,15 USD")
selector()