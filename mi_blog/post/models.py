from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image=models.ImageField(upload_to ='images/',default="")
    titulo = models.CharField(max_length=200)
    articulo = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
