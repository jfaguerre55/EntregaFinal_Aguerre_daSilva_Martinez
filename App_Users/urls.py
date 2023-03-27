from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='App_Services/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('editar-perfil/', UsuarioEdicion.as_view(), name='editar-perfil'),
    path('password-cambio/', CambioPassword.as_view(), name='cambiar-password'),
    path('password-exitoso/' , password_exitoso, name='password-exitoso'),
    path('avatar-create/', AvatarCreate.as_view(), name='avatar-create'),
    path('avatar-update/<int:pk>/', AvatarUpdate.as_view(), name='avatar-update'),

]
