from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Autor)
admin.site.register(models.Categorias)
admin.site.register(models.Publicaciones)
admin.site.register(models.Libro)