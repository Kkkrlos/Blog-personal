"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name="main"),
    path('publicaciones/', views.post_detail, name="post_detail"),
    path('publicacion/<int:id>', views.Post, name="Post"),
    path('libros/', views.Libros, name="libros"),
    path('https://www.linkedin.com/in/carlosrodriguez1205/', views.Linkedin, name="Linkedin"),
    path('https://github.com/Kkkrlos', views.Github, name="Github")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
