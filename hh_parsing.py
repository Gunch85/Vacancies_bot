import requests
import time
import json


vacancies_ids = set()


def get_page(page=0):

    params = {
        'text': 'Водитель',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 1002,  # Поиск ощуществляется по вакансиям города Минск
        'salary': 1500,  # Заработная плата
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'period': 1
    }

    req = requests.get('https://api.hh.ru/vacancies', params=params)
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


def parse_data():
    lst_objs, new_objs = [], []
    for i in range(11):
        json_data = get_page(i)
        jsobj = json.loads(json_data)
        lst_objs.extend(jsobj['items'])

        time.sleep(0.25)

    for obj in lst_objs:
        if obj['id'] not in vacancies_ids:
            new_objs.append(obj)
        vacancies_ids.add(obj['id'])

    return new_objs