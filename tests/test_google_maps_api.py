import pytest
from utils.api import Google_maps_api
from requests import Response
from utils.checking import *
import allure


"""Создание, изменение и удаление новой локи"""
@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update, delete new place")
    def test_create_place(self):

        print('Метод POST ')
        res_post: Response = Google_maps_api.create_new_place()
        check_post = res_post.json()
        place_id = check_post.get("place_id")
        token_post = ['status', 'place_id', 'scope', 'reference', 'id']
        Checking.check_status_code(res_post, 200)
        Checking.check_json_token(res_post, token_post)
        Checking.check_json_value(res_post,'status','OK')

        print('Метод GET - после POST')
        res_get: Response = Google_maps_api.get_new_place(place_id)
        #print(list(res_get.json()))
        token_get = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        Checking.check_status_code(res_get, 200)
        Checking.check_json_token(res_get, token_get)
        Checking.check_json_value(res_get,'address','29, side layout, cohen 09')

        print('Метод PUT')
        print(f'Передаваемый place_id: {place_id}')
        new_address = "100 Lenina street, RU"
        res_put: Response = Google_maps_api.upd_place(place_id, new_address)
        Checking.check_status_code(res_put, 200)
        Checking.check_json_token(res_put, ['msg'])
        Checking.check_json_value(res_put,'msg','Address successfully updated')

        print('Метод GET - после PUT')
        res_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(res_get, 200)
        Checking.check_json_token(res_get, token_get)
        Checking.check_json_value(res_get,'address',new_address)

        print('Метод DELETE')
        res_delete: Response = Google_maps_api.delete_place(place_id)
        Checking.check_status_code(res_delete, 200)
        Checking.check_json_token(res_delete, ['status'])
        Checking.check_json_value(res_delete,'status','OK')

        print('Метод GET - после DELETE')
        res_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(res_get, 404)
        Checking.check_json_token(res_get, ['msg'])
        Checking.check_json_value(res_get,'msg',"Get operation failed, looks like place_id  doesn't exists")
        

        print("Тестирование создания, изменения и удаления новой локации прошло успешно!")
