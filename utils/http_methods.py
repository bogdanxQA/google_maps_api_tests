import requests
from utils.logger import Logger
import allure

""""Список HTTP методов"""
class http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            res = requests.get(url, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(res)
            return res
    
    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            res = requests.post(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(res)
            return res
    
    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            res = requests.put(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(res)
            return res
    
    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            res = requests.delete(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(res)
            return res
    

        
    