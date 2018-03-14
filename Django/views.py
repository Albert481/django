from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'registration/../templates/login.html')

def logout(request):
    return render(request, 'logout.html')