from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    imagen_avatar = models.ImageField(null=True, blank=True, upload_to='imagenes/')

    def __str__(self) -> str:
        return self.usuario.username
    
