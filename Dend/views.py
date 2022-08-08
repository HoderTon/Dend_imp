from django.http import HttpResponse
from django.shortcuts import render
from datetime import today
import json


def index(request):
    try:
        with open('track.json', 'w') as file:
            json.dump({'date': today.strftime("%B %d, %Y"), 'time': }
                      |{'status_code': HttpResponse.status_code}
                      | dict(request.headers), file)
        return HttpResponse('Request saved as "track.json"')
    except:
        return HttpResponse('Error while working with file')