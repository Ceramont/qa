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

    def get_joke(self, base):
        for category in self.get_categories(base):
            load = f"/random?category={category}"
            result = requests.get(base + load)
            assert 200 == result.status_code
            print_result = result.json()
            print("Категория: " + print_result["categories"][0] + ", Шуточка: " + print_result["value"])


joke = Request()
joke.get_joke(base_url)
