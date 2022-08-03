# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current time is {now}'.format(now=now))

def hi(request):
    scheme = request.scheme # http
    path = request.path # /hi/
    method = request.method # GET
    body = request.body # Body
    cookies = request.COOKIES
    meta = request.META  # all available HTTP headers.
    
    return HttpResponse(meta)