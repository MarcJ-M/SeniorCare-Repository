from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django. contrib import messages
from .models import senior_list
from .forms import register_form
# Create your views here.

def index(request):
    return render(request, 'index.html'  )

def index(request):
    page='index'
    if request.method =='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'User does not exist') #if the user does not exist

        user=authenticate(request, username=username, password=password) #to make sure the credentials are correct

        if user is not None:
            login(request, user)
            return redirect(home_page)
        else:
            messages.error(request, 'Invalid Username and Password') #if the user does not exist
    context ={'page':page}
    return render(request, 'index.html', context)

def home_page(request):
    return render(request, 'home_page.html'  )

def register_page(request):
    return render(request, 'register_page.html')

def main_page(request):
    return render(request, 'main.html')

def register_page(request):
    form = register_form()
    if request.method =='POST':
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(register_page)
    context={'form':form}
    return render(request, 'register_page.html', context)

def update_page(request):
    return render(request, 'update_page.html')

def update_viewinfo_page(request):
    return render(request, 'update_viewinfo_page.html')