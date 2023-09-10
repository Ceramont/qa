import requests
import numpy as np


class Request:

    def __init__(self):
        pass

    """Метод очистки файла"""
    @staticmethod
    def file_update():
        with open("places.txt", "w", newline='') as file:
            print("Файл places очищен ")
        with open("ex_places.txt", "w", newline='') as file:
            print("Файл ex_places очищен")

    """Метод для записи place_id в файл"""
    @staticmethod
    def input_place_id(place_id, name):
        with open(name, "a", newline='') as file:
            file.write(place_id + "\n")

    """Метод для чтения из файла"""
    @staticmethod
    def file_read():
        with open("places.txt", "r", newline='') as file:
            return file.read().splitlines()

    """Метод для отправки Post запроса на создание локации"""
    def delete_place(self, base):
        api_load = "/maps/api/place/delete/json"
        key_load = "?key=qaclick123"
        res_url = base + api_load + key_load
        place_ids = np.array(self.file_read())[[1, 3]]
        for place_id in place_ids:
            json = {
                "place_id": place_id
            }
            res = requests.delete(res_url, json=json)
            assert "OK" == res.json()["status"]
            print(f"""Локация с place_id: {place_id} успешно удалена.""")

    """Метод отправки Get запроса для проверки существования place_id"""
    def get_places(self, base):
        with open("places.txt", "r", newline='') as file:
            api_load = "/maps/api/place/get/json?key=qaclick123&place_id="
            place_ids = file.read().splitlines()
            for place_id in place_ids:
                res_url = base + api_load + place_id
                res_get = requests.get(res_url)
                if res_get.status_code == 200:
                    self.input_place_id(place_id, "ex_places.txt")
                    print(f"""Локация с place_id: {place_id} существует и добавлена в файл.""")
                else:
                    print(f"""Локация с place_id: {place_id} не существует""")

    """Метод для отправки Post запроса на создание локации"""
    def post_place(self, base, json):
        for i in range(5):
            api_load = "/maps/api/place/add/json"
            key_load = "?key=qaclick123"
            res_url = base + api_load + key_load
            res = requests.post(res_url, json=json)
            assert "OK" == res.json()["status"]
            print(f"""Локация с place_id: {res.json()["place_id"]} успешно cоздана.""")
            self.input_place_id(res.json()["place_id"], "places.txt")


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
gmap.delete_place(base_url)
gmap.get_places(base_url)

