"""методы для тестирования google maps api"""
from utils.http_methods import http_methods

base_url = "https://rahulshettyacademy.com"
querys = "?key=qaclick123"
class Google_maps_api():
    
    @staticmethod
    def create_new_place():

        json_for_create_place = {
            "location": { 
            "lat": -38.383494, 
            "lng": 33.427362 
            }, "accuracy": 50, 
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
        post_resource = "/maps/api/place/add/json"
        post_url = f"{base_url}{post_resource}{querys}"
        print(f'Запрос отправлен по данному URL: {post_url}')
        res_post = http_methods.post(post_url,json_for_create_place)
        print(f"Тело ответа: {res_post.text}")
        return res_post

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json" 
        get_url = f"{base_url}{get_resource}{querys}&place_id={place_id}"
        print(f'Запрос отправлен по данному URL: {get_url}')
        res_get = http_methods.get(get_url)
        print(f"Тело ответа: {res_get.text}")
        return res_get
    
    @staticmethod
    def upd_place(place_id,new_address):
        put_resource = "/maps/api/place/update/json"
        put_url = f"{base_url}{put_resource}{querys}"
        print(f'Запрос отправлен по данному URL: {put_url}')
        json_for_update = {"place_id":f"{place_id}",
                                "address":f"{new_address}", 
                                "key":"qaclick123"
            

        }
        res_put = http_methods.put(put_url, json_for_update)
        #print(json_for_update)
        print(f"Тело ответа: {res_put.text}")
        return res_put
    

    @staticmethod
    def delete_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{base_url}{delete_resource}{querys}"
        print(f'Запрос отправлен по данному URL: {delete_url}')
        json_for_delete = {
            "place_id":f"{place_id}" 
        }
        res_delete = http_methods.delete(delete_url, json_for_delete)
        print(f"Тело ответа: {res_delete.text}")
        return res_delete
