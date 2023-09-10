import json


class Check:

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result
        print(f"""Успешно статус код: {status_code}""")

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        assert result.json()[field_name] == expected_value
        print("Значения верны")