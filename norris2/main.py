import requests
base_url = "https://api.chucknorris.io/jokes"


class Request:

    def __init__(self):
        pass

    @staticmethod
    def get_categories(base):
        load = "/categories"
        result = requests.get(base + load)
        assert 200 == result.status_code
        print("Категории успешно получены")
        return result.json()

    @staticmethod
    def get_joke(base, input_category):
        load = f"/random?category={input_category}"
        result = requests.get(base + load)
        assert 200 == result.status_code
        print_result = result.json()
        print("Категория: " + print_result["categories"][0] + ", Шуточка: " + print_result["value"])

    def input_category(self, base):
        categories = self.get_categories(base)
        try:
            print("Введите категорию:")
            input_category = input()
            if input_category in categories:
                self.get_joke(base, input_category)
            else:
                print("Нет такой категории")
        except:
            print("Неверный формат")


joke = Request()
joke.input_category(base_url)
