from django.db import models
from django.contrib.auth.models import User

# Modelo de servicio que se puede ofrecer
class Servicio(models.Model):
    servicioSeleccion = (
    ('impresion3D','Impresion3D'),
    ('escaneo3D', 'Escaneo3D'),
    ('software','Software'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    servicio = models.CharField(max_length=15, choices=servicioSeleccion, default='impresion3D')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    anio = models.IntegerField() 
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    telefono_contacto = models.IntegerField()
    email_contacto = models.EmailField()
    imagen_servicio = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fecha_publicacion']

    def __str__(self):
        return self.titulo




class Comentario(models.Model):
    comentario = models.ForeignKey(Servicio, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_comentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
