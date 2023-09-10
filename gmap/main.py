import requests


class Request:

    def __init__(self):
        pass

    """Метод очистки файла"""
    @staticmethod
    def file_update():
        with open("places.txt", "w", newline='') as file:
            print("Файл очищен")

    """Метод для записи новых place_id в файл"""
    def input_place_id(self, place_id):
        with open("places.txt", "a", newline='') as file:
            file.write(place_id + "\n")

    """Метод отправки Get запроса для проверки существования place_id"""
    @staticmethod
    def get_places(base):
        with open("places.txt", "r", newline='') as file:
            api_load = "/maps/api/place/get/json?key=qaclick123&place_id="
            place_ids = file.read().splitlines()
            for place_id in place_ids:
                res_url = base + api_load + place_id

                res_get = requests.get(res_url)

                assert 200 == res_get.status_code
                print(f"""Локация с place_id: {place_id} существует.""")

    """Метод для отправки Post запроса на создание локации"""
    def post_place(self, base, json):
        for i in range(5):
            api_load = "/maps/api/place/add/json"
            key_load = "?key=qaclick123"
            res_url = base + api_load + key_load
            res = requests.post(res_url, json=json)
            assert "OK" == res.json()["status"]
            print(f"""Локация с place_id: {res.json()["place_id"]} успешно cоздана.""")
            self.input_place_id(res.json()["place_id"])


base_url = "https://rahulshettyacademy.com"
json_load = {
    "location": {
        "lat": -38.383494,
        "lng": 33.427362
    },
    "accuracy": 50,
    "name": "Frontline house",
    "phone_number": "(+91) 983 893 3937",
    "address": "29, side layout, cohen 09",
    "types": [
        "shoe park",
        "shop"
    ],
    "website": "http://google.com",
    "language": "French-IN"
}
gmap = Request()
gmap.file_update()
gmap.post_place(base_url, json_load)
gmap.get_places(base_url)

