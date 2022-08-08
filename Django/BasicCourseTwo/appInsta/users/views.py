"""Users views"""
# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    """Login view

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html', {'error': 'Invalid username and password'})
        
    return render(request, 'users/login.html')