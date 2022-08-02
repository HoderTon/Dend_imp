from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    try:
        with open('track.json', 'w') as file:
            file.write(str(request.headers))
        return HttpResponse('Запрос сохранён в файл track.json')
    except:
        return HttpResponse('Ошибка при работе с файлом')