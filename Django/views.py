from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/../templates/login.html')

def logout(request):
    return render(request, 'logout.html')