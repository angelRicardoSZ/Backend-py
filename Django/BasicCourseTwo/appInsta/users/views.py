"""Users views"""
# Django
import profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.shortcuts import render, redirect


# Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm


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
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html', {'error': 'Invalid username and password'})
        
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation = request.POST['password_confirmation']

        # PASSWORD VALIDATION
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})    
        # USERNAME VALIDATION
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('feed')

    return render(request, 'users/signup.html')

@login_required
def update_profile(request):
    """_summary_

    Args:
        request (_type_): _description_
    """
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()
            
    profile = request.user.profile
    
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form
        })


