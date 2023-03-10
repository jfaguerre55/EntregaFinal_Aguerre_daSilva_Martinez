from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 

from .models import Servicio, Comentario




# COMENTARIOS

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }




# SERVICIOS 

class FormularioNuevoServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('usuario', 'titulo', 'servicio', 'marca', 'modelo', 'descripcion', 'anio', 'telefono_contacto', 'email_contacto', 'imagen_servicio')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'servicio' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'anio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_contacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'email_contacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizacionServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('titulo', 'servicio', 'marca', 'modelo', 'descripcion', 'anio', 'telefono_contacto', 'email_contacto', 'imagen_servicio')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'servicio' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'anio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_contacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'email_contacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }

