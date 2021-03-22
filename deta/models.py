from django.db import models
from django.urls import reverse

# Create your models here.

class Entre(models.Model):
    juego = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    nombre = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    Descripcion = models.TextField()

    def __str__(self):
        return self.juego

    def get_absolute_url(self):
        return reverse('archivo', args=[str(self.id)])

    fotos = models.CharField(max_length=100, default='')
   

        

    