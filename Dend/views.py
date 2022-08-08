from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import json


def index(request):
    try:
        with open('track.json', 'w') as file:
            json.dump({'Date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                       'status_code': HttpResponse.status_code} | dict(request.headers), file)
        return HttpResponse('Request saved as "track.json"')
    except:
        return HttpResponse('Error while working with file')