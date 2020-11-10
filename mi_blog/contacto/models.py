from django.db import models
from django.utils import timezone
# Create your models here.


class Contacto(models.Model):
    nombre= models.CharField(max_length=200)
    email=models.EmailField()
    mensaje = models.TextField()
    fecha_de_contacto = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
