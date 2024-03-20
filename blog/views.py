from django.shortcuts import render, redirect
from .models import Publicaciones
# Create your views here.

def IndexView(request):
    publicaciones = Publicaciones.objects.all()
    return render(request, 'main.html', {'publicaciones': publicaciones})

def post_detail(request):
    publicaciones = Publicaciones.objects.all()
    return render(request, 'post_detail.html', {'publicaciones': publicaciones})

def Linkedin(request):
    return redirect('https://www.linkedin.com/in/carlosrodriguez1205/')

def Github(request):
    return redirect('https://github.com/Kkkrlos')