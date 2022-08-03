# Django
from email import message
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current time is {now}'.format(now=now))

def hi(request):
    # scheme = request.scheme # http
    # path = request.path # /hi/
    # method = request.method # GET
    # body = request.body # Body
    # cookies = request.COOKIES
    # meta = request.META  # all available HTTP headers.
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers':sorted_ints,
        'message':'Integers sorted successfully.'
    }
    
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    """Return a string 

    Args:
        
        name (str): username
        age (int): user age
    # """
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {} '.format(name)
    
    return HttpResponse(message)