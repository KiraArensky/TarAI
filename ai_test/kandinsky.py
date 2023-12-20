import requests

import json
import time
import base64

from random import randint as r
from random import choice as ch

import os


class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=576, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


def gen(prom, dirr="taro_card_ai_ru"):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '70E8A6D7EB3702C3B1578786AE4FD197',
                        'F196BDDF4ABDB74C8570FEA4366AC99F')
    model_id = api.get_model()
    uuid = api.generate(prom, model_id)
    images = api.check_generation(uuid)

    # Здесь image_base64 - это строка с данными изображения в формате base64
    image_base64 = images[0]

    # Декодируем строку base64 в бинарные данные
    image_data = base64.b64decode(image_base64)

    # Открываем файл для записи бинарных данных изображения
    try:
        with open(f"{dirr}/{prom.split('.')[0]} _ {r(0, 100000)}.jpg", "wb") as file:
            file.write(image_data)
    except:
        with open(f"{dirr}/{prom.split('.')[0]} _ {r(0, 100000)}.jpg", "w+") as file:
            file.write(image_data)


tarot_deck_en = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
    "Ace of Wands",
    "Two of Wands",
    "Three of Wands",
    "Four of Wands",
    "Five of Wands",
    "Six of Wands",
    "Seven of Wands",
    "Eight of Wands",
    "Nine of Wands",
    "Ten of Wands",
    "Page of Wands",
    "Knight of Wands",
    "Queen of Wands",
    "King of Wands",
    "Ace of Cups",
    "Two of Cups",
    "Three of Cups",
    "Four of Cups",
    "Five of Cups",
    "Six of Cups",
    "Seven of Cups",
    "Eight of Cups",
    "Nine of Cups",
    "Ten of Cups",
    "Page of Cups",
    "Knight of Cups",
    "Queen of Cups",
    "King of Cups",
    "Ace of Swords",
    "Two of Swords",
    "Three of Swords",
    "Four of Swords",
    "Five of Swords",
    "Six of Swords",
    "Seven of Swords",
    "Eight of Swords",
    "Nine of Swords",
    "Ten of Swords",
    "Page of Swords",
    "Knight of Swords",
    "Queen of Swords",
    "King of Swords",
    "Ace of Pentacles",
    "Two of Pentacles",
    "Three of Pentacles",
    "Four of Pentacles",
    "Five of Pentacles",
    "Six of Pentacles",
    "Seven of Pentacles",
    "Eight of Pentacles",
    "Nine of Pentacles",
    "Ten of Pentacles",
    "Page of Pentacles",
    "Knight of Pentacles",
    "Queen of Pentacles",
    "King of Pentacles"
]

tarot_deck_ru = [
    "Безумец",
    "Маг",
    "Верховная Жрица",
    "Императрица",
    "Император",
    "Жрец",
    "Влюбленные",
    "Колесница",
    "Сила",
    "Отшельник",
    "Колесо Фортуны",
    "Правосудие",
    "Повешенный",
    "Смерть",
    "Умеренность",
    "Дьявол",
    "Башня",
    "Звезда",
    "Луна",
    "Солнце",
    "Суд",
    "Мир",
    "Туз Жезлов",
    "Два Жезла",
    "Три Жезла",
    "Четыре Жезла",
    "Пять Жезлов",
    "Шесть Жезлов",
    "Семь Жезлов",
    "Восемь Жезлов",
    "Девять Жезлов",
    "Десять Жезлов",
    "Паж Жезлов",
    "Рыцарь Жезлов",
    "Королева Жезлов",
    "Король Жезлов",
    "Туз Чаш",
    "Два Чаш",
    "Три Чаш",
    "Четыре Чаш",
    "Пять Чаш",
    "Шесть Чаш",
    "Семь Чаш",
    "Восемь Чаш",
    "Девять Чаш",
    "Десять Чаш",
    "Паж Чаш",
    "Рыцарь Чаш",
    "Королева Чаш",
    "Король Чаш",
    "Туз Мечей",
    "Два Мечей",
    "Три Мечей",
    "Четыре Меча",
    "Пять Мечей",
    "Шесть Мечей",
    "Семь Мечей",
    "Восемь Мечей",
    "Девять Мечей",
    "Десять Мечей",
    "Паж Мечей",
    "Рыцарь Мечей",
    "Королева Мечей",
    "Король Мечей",
    "Туз Пентаклей",
    "Два Пентаклей",
    "Три Пентаклей",
    "Четыре Пентаклей",
    "Пять Пентаклей",
    "Шесть Пентаклей",
    "Семь Пентаклей",
    "Восемь Пентаклей",
    "Девять Пентаклей",
    "Десять Пентаклей",
    "Паж Пентаклей",
    "Рыцарь Пентаклей",
    "Королева Пентаклей",
    "Король Пентаклей"
]

print('start')
for i in tarot_deck_ru:
    zapros = f'Tarot {i}'
    gen(zapros.replace("\n", " "))
    print(f"done {i}")

print("all done")
