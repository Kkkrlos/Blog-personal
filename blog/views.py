from django.shortcuts import render, redirect

# Create your views here.

def IndexView(request):
    return render(request, 'index.html')

def Linkedin(request):
    return redirect('https://www.linkedin.com/in/carlosrodriguez1205/')

def Github(request):
    return redirect('https://github.com/Kkkrlos')