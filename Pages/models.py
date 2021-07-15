from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Nombre')
    description = models.CharField(max_length=255, verbose_name = 'Descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    content = RichTextField (verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")
    slug = models.CharField(unique= True, max_length=150, verbose_name='Url_Amigable')
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False,on_delete=models.CASCADE) # Clave ajena de User, Con el uso de editable quitamos la opcion de elegir el usuario en los articulos
    categories = models.ManyToManyField(Category, default='None',verbose_name='Categorias', blank=True) # Clave ajena de Category
    public = models.BooleanField(verbose_name='Publico')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title