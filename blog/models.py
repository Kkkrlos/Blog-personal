from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(verbose_name="Nombre")
    icono_perfil =  models.ImageField(verbose_name="Icono de perfil",upload_to='iconos_perfil')
    about_me = models.TextField(verbose_name="Descripción", null=False, blank=False)

    def __str__(self) -> str:
        return self.nombre

class Categorias(models.Model):
    nombre = models.CharField(verbose_name="Nombre de la categoría")

    def __str__(self) -> str:
        return self.nombre

class Publicaciones(models.Model):
    titulo = models.CharField(verbose_name="Título de la publicación")
    imagen = models.ImageField(verbose_name="Imagen para la publicación", upload_to="posts", null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripción de la publicación")
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de publicación", auto_now=True)

    def __str__(self) -> str:
        return self.titulo