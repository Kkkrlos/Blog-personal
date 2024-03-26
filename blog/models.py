from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(verbose_name="Nombre")
    foto_perfil = models.ImageField(verbose_name="Foto de perfil del autor")
    icono_perfil =  models.ImageField(verbose_name="Icono de perfil", upload_to='iconos_perfil')
    about_me = models.TextField(verbose_name="Descripción", null=False, blank=False)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.nombre

class Categorias(models.Model):
    nombre = models.CharField(verbose_name="Nombre de la categoría")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self) -> str:
        return self.nombre


class Publicaciones(models.Model):
    titulo = models.CharField(verbose_name="Título de la publicación")
    imagen = models.ImageField(verbose_name="Imagen para la publicación", upload_to="posts", null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripción de la publicación")
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de publicación", auto_now=True)

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self) -> str:
        return self.titulo

class Libro(models.Model):
    portada = models.ImageField(verbose_name="Portada del libro", upload_to="portadas_libros")
    titulo = models.CharField(verbose_name="Título del libro", blank=False, max_length=100)
    autor = models.CharField(verbose_name="Autor del libro")
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    descripcion  = models.TextField(verbose_name="Descripción del libro")
    archivo = models.FileField(verbose_name="PDF/Epub del libro", upload_to="pdfs")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self) -> str:
        return self.titulo