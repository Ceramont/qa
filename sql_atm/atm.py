from sql_querry import SQL_atm


class ATM:

    def atm_logic(self):

        # SQL_atm.create_table()
        # SQL_atm.insert_users((2345, 2222, 10000))
        number_card = input("Введите номер карты:")
        # SQL_atm.report_operation_2()
        while True:
            if SQL_atm.input_card(number_card):
                if SQL_atm.input_code(number_card):
                    SQL_atm.input_operation(number_card)
                    break
            else:
                break


start = ATM()
start.atm_logic()
