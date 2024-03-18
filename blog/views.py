from django.shortcuts import render, redirect

# Create your views here.

def IndexView(request):
    return render(request, 'main.html')

def post_detail(request):
    return render(request, 'post_detail.html')

def Linkedin(request):
    return redirect('https://www.linkedin.com/in/carlosrodriguez1205/')

def Github(request):
    return redirect('https://github.com/Kkkrlos')