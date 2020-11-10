from django.db import models

# Create your models here.

class Contacto(models.Model):
    titulo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    mensaje=models.TextField()


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Contactos"

class Image(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='images')


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Imagenes"
