import json
from utils.api import Google_maps_api
from utils.checking import Check
import allure


@allure.epic("Test create place")
class Test_create_place:

    @allure.description("Test create new place")
    def test_create_new_place(self):
        # Получение всех полей
        # print(json.фддгкуloads(result_get.text))
        print("POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post["place_id"]
        Check.check_status_code(result_post.status_code, 200)
        Check.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Check.check_json_value(result_post, 'status', 'OK')
        print("GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Check.check_status_code(result_get.status_code, 200)
        Check.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        print("PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Check.check_status_code(result_put.status_code, 200)
        Check.check_json_token(result_put, ['msg'])
        Check.check_json_value(result_put, 'msg', 'Address successfully updated')
        print("GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Check.check_status_code(result_get.status_code, 200)
        Check.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_json_value(result_get, 'address', '100 Lenina street, RU')
        print("DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Check.check_status_code(result_delete.status_code, 200)
        Check.check_json_token(result_delete, ['status'])
        Check.check_json_value(result_delete, 'status', 'OK')
        print("GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Check.check_status_code(result_get.status_code, 404)
        Check.check_json_token(result_get, ['msg'])
        Check.check_json_value(result_get, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')
        print("Тестирование создания, удаления, изменения новой локации прошло успешно")
