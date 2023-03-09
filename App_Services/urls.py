from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='App_Services/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicion-perfil/', UsuarioEdicion.as_view(), name='editar-perfil'),
    path('password-cambio/', CambioPassword.as_view(), name='cambiar-password'),
    path('password-exitoso/' , views.password_exitoso, name='password-exitoso'),

    path('creacion-servicio/', ServicioCreacion.as_view(), name='creacion-servicio'),
    path('acerca-de-nosotros/', views.about, name='acerca-de-nosotros'),

    path('impresion3d-lista/', Impresion3DLista.as_view(), name='impresion3d-lista'),
    path('escaneo3d-lista/', Escaneo3DLista.as_view(), name='escaneo3d-lista'),
    path('software-lista/', SoftwareLista.as_view(), name='software-lista'),
    path('otros-lista/', OtrosLista.as_view(), name='otros-lista'),

    path('impresion3d-detalle/<int:pk>/', Impresion3DDetalle.as_view(), name='impresion3d-detalle'),
    path('escaneo3d-detalle/<int:pk>/', Escaneo3DDetalle.as_view(), name='escaneo3d-detalle'),
    path('software-detalle/<int:pk>/', SoftwareDetalle.as_view(), name='software-detalle'),
    path('otros-detalle/<int:pk>/', OtrosDetalle.as_view(), name='otros-detalle'),

    path('impresion3d-editar/<int:pk>/', Impresion3DUpdate.as_view(), name='impresion3d-editar'),
    path('escaneo3d-editar/<int:pk>/', Escaneo3DUpdate.as_view(), name='escaneo3d-editar'),
    path('software-editar/<int:pk>/', SoftwareUpdate.as_view(), name='software-editar'),
    path('otros-editar/<int:pk>/', OtrosUpdate.as_view(), name='otros_editar'),

    path('impresion3d-borrar/<int:pk>/', Impresion3DDelete.as_view(), name='impresion3d-borrar'),
    path('escaneo3d-borrar/<int:pk>/', Escaneo3DDelete.as_view(), name='escaneo3d-borrar'),
    path('software-borrar/<int:pk>/', SoftwareDelete.as_view(), name='software-borrar'),
    path('otros-borrar/<int:pk>/', OtrosDelete.as_view(), name='otros-borrar'),

    path('impresion3d-detalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('escaneo3d-detalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('software-detalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otros-detalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    
]
