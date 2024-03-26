from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicaciones, Autor, Libro
# Create your views here.

def IndexView(request):
    publicaciones = Publicaciones.objects.all()
    return render(request, 'main.html', {'publicaciones': publicaciones})

def post_detail(request):
    publicaciones = Publicaciones.objects.all()
    return render(request, 'post_detail.html', {'publicaciones': publicaciones})

def Post(request, id):
    publicacion = get_object_or_404(Publicaciones, pk=id)
    return render(request, "post_id.html", {'publicacion': publicacion})

def Libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html' ,{"libros": libros})

def Linkedin(request):
    return redirect('https://www.linkedin.com/in/carlosrodriguez1205/')

def Github(request):
    return redirect('https://github.com/Kkkrlos')