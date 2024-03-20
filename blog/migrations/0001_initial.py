# Generated by Django 5.0.3 on 2024-03-19 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(verbose_name='Nombre')),
                ('icono_perfil', models.ImageField(upload_to='iconos_perfil', verbose_name='Icono de perfil')),
                ('about_me', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(verbose_name='Nombre de la categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Descripción de la publicación')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha de publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categorias')),
            ],
        ),
    ]
