import sqlite3 as sql


# Функция выбора действия
def selector():
    print("Введите действие которое хотите совершить (Регистрация[1], Авторизация[2], Сменя пароля[3])")
    try:
        s = int(input())
    except ValueError:
        s = -1

    while s != 1 and s != 2 and s != 3:
        print("Необходимо ввести либо 1, либо 2, либо 3")
        try:
            s = int(input())
        except ValueError:
            s = -1
    #Вызов выбранной функции
    if s == 1:
        register()
    elif s == 2:
        login()
    elif s == 3:
        change_password()


# Функция Авторизации
def login():
    print("Вы выбрали модуль Авторизация")
    print("Введите ваш Логин")
    # Ввод логина из cmd
    user_login = input()
    # Первичный запрос к бд для проверки существования строки где Логин = введенному логину
    cur.execute(f"SELECT * FROM users_data WHERE Login = '{user_login}'")
    res_exec = cur.fetchone()
    # Пока введенный логин не пуст или результирующая строка запроса пуста, продолжаем вводить логин
    while len(user_login) == 0 or res_exec is None:
        if len(user_login) == 0:
            print("Логин не может быть пустым")
        elif res_exec is None:
            print("Данный пользователь не существует")
        user_login = input()
        cur.execute(f"SELECT UserID FROM users_data WHERE Login = '{user_login}'")
        res_exec = cur.fetchone()
    print("Введите пароль")
    user_password = str(input())
    # Пока пароль не пуст или пароль неправильный продолжаем ввод
    while user_password != res_exec[2] or len(str(user_password)) == 0:
        if len(str(user_password)) == 0:
            print("Пароль не может быть пустым")
        elif user_password != res_exec[2]:
            print("Введен неправильный пароль")
        user_password = str(input())
    print("Вы успешно авторизованы")
    selector()


# Функция регистрации
def register():
    # Лист для результирующего запроса
    reg_data = []
    print("Вы выбрали модуль регистрация")
    print("Введите логин, который вы хотите использовать")
    user_login = input()
    # Проверка что логин уникален
    cur.execute(f"SELECT UserID FROM users_data WHERE Login = '{user_login}'")
    res_login = cur.fetchone()

    while len(user_login) == 0 or res_login is not None:
        if len(user_login) == 0:
            print("Логин не может быть пустым")
        elif res_login is not None:
            print("Данное имя занято, введите другое")
        user_login = input()
        cur.execute(f"SELECT UserID FROM users_data WHERE Login = '{user_login}'")
        res_login = cur.fetchone()
    reg_data.append(user_login)
    print("Введите пароль (до 10 символов)")
    user_password = input()
    # Пока пароль пустой или больше 10 символов (Добавил от себя данное условие) продолжаем вводить
    while len(user_password) == 0 or len(str(user_password)) > 10:
        if len(user_password) == 0:
            print("Пароль не может быть пустым")
        elif len(user_password) > 11:
            print("Пароль должен быть не более 10 символов")
        user_password = input()
    reg_data.append(user_password)
    print("Введите секретный 4-х значный код для восстановления пароля")
    # Проверка на число
    try:
        user_pin = int(input())
    except ValueError:
        user_pin = 1
    # Пока длина числа не равна 4 продолжаем вводить
    while len(str(user_pin)) != 4:
        print("Код должен быть 4-x значным числом (От 1000-9999)")
        try:
            user_pin = int(input())
        except ValueError:
            user_pin = 1
    reg_data.append(user_pin)
    # Финальный запрос на добавление новой строки с пользователем
    try:
        cur.execute("""INSERT INTO users_data(Login,Password,Code) VALUES (?,?,?)""", reg_data)
    except Exception:
        print("Регистрация прошла неудачно")
    db.commit()
    # Проверяем создался ли пользователь
    cur.execute(f"SELECT UserID FROM users_data WHERE Login = '{reg_data[0]}'")
    if cur.fetchone() is not None:
        print("Регистрация успешно выполнено")
        selector()

# Функция Смены пароля
def change_password():
    print("Вы выбрали модуль Восстановления пароля")

    print("Введите ваш Логин")
    user_login = input()
    # Достаем из бд строку с подходящим логином для проверки существования пользователя
    cur.execute(f"SELECT * FROM users_data WHERE Login = '{user_login}'")
    res_exec = cur.fetchone()
    while len(user_login) == 0 or res_exec is None:
        if len(user_login) == 0:
            print("Логин не может быть пустым")
        elif res_exec is None:
            print("Данный пользователь не существует")
        user_login = input()
        cur.execute(f"SELECT UserID FROM users_data WHERE Login = '{user_login}'")
        res_exec = cur.fetchone()

    print("Введите 4-х значный код для восстановления")
    # Ввод пинкода
    try:
        user_pin = int(input())
    except ValueError:
        user_pin = 1
    # Проверка что введенный код является 4 значным числом и совпадает с тем что в бд
    while int(user_pin) != res_exec[3] or len(str(user_pin)) != 4:
        if len(str(user_pin)) != 4:
            print("Код должен быть 4-x значным числом (От 1000-9999)")
        elif int(user_pin) != res_exec[3]:
            print("Введен неправильный код")
        try:
            user_pin = int(input())
        except ValueError:
            user_pin = 1
    print("Введите новый пароль (до 10 символов)")
    user_password = input()
    while len(user_password) == 0 or len(str(user_password)) > 10:
        if len(user_password) == 0:
            print("Пароль не может быть пустым")
        elif len(user_password) > 11:
            print("Пароль должен быть не более 10 символов")
        user_password = input()
    cur.execute(f"UPDATE users_data SET Password = '{user_password}' WHERE UserID = '{res_exec[0]}'")
    db.commit()
    print("Пароль успешно обновлен")
    selector()
# Точка входа в приложение
# Подключение к бд
try:
    db = sql.connect('registration.db')
    cur = db.cursor()
    print("Подключение к бд выполнено")
except Exception:
    print("Подключение к бд не выполнено")

"""Первичное создание таблицы с добавлением 1 пользователя """
# user_data_param = ('Ivan', 'qwer1234', 1234)
# cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
# UserID INTEGER PRIMARY KEY AUTOINCREMENT,
# Login TEXT NOT NULL,
# Password TEXT NOT NULL,
# Code INTEGER NOT NULL);""")
#
# cur.execute("""INSERT INTO users_data(Login,Password,Code)
# VALUES (?,?,?)""", user_data_param)
# db.commit()
"""Запуск функции выбора действия"""
selector()



