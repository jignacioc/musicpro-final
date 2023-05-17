from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def signin(request):
    return render(request, 'core/signin.html')

def aboutus(request):
    return render(request, 'core/about-us.html')

def base(response):
    return redirect("index")