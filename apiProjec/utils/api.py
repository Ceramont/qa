from utils.http_methods import Http_method

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class Google_maps_api():

    @staticmethod
    def create_new_place():
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        json_for_create_new_location = {
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
        result = Http_method.post(post_url, json_for_create_new_location)
        print(post_url)
        print(result.json())
        return result

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        result = Http_method.get(get_url)
        print(get_url)
        print(result.json())
        return result

    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {

            "place_id": place_id,

            "address": "100 Lenina street, RU",

            "key": "qaclick123"

        }
        result = Http_method.put(put_url, json_for_update_new_location)
        print(result.json())
        return result

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        put_url = base_url + delete_resource + key
        print(put_url)
        json_for_delete_new_location = {

            "place_id": place_id

        }
        result = Http_method.put(put_url, json_for_delete_new_location)
        print(result.json())
        return result
