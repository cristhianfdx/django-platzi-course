# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current time in server is {}'.format(str(now)))


def sorted_nums(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'sorted integers'
    }

    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
        )


def hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to platzigram'.format(name)

    return HttpResponse(message)
