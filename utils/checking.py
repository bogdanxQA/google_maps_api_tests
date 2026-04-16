"""Методы для проверки ответов запросов"""

from requests import Response


class Checking():
    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f'Провал! Статус код {response.status_code} не соответствует ожидаемому: {status_code}'
        print(f'Успешно! Статус код: {response.status_code} соответствует ожидаемому {status_code}')

    """"Проверка обязательных полей в ответе"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = response.json()
        assert list(token) == expected_value, 'Отсутствуют обязательные поля'
        print('Все обязателньые поля присутствуют')

    """Проверка значения полей в ответе"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f'значение поля {field_name} = {check_info} не совпадает с ожидаемым - {expected_value}'
        print(f'Значение поля {field_name} - верно')





  