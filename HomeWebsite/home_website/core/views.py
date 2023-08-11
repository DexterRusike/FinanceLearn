from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'core/index.html')



@login_required
def user_logout(request):
     logout(request)
     return redirect('/')


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            print(f'Username:{username} and password {password}')
            return HttpResponse('Invalid login details provided')
    else:
        return render(request, 'core/login.html',{})