from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin 

from .models import Servicio, Comentario


# USUARIOS 

class FormularioRegistroUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'nombre', 'apellido', 'password1', 'password2')



class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    nombre = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'nombre', 'apellido')



class FormularioCambioPassword(PasswordChangeForm):
    old_pass = forms.CharField(label=("Contraseña actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_pass1 = forms.CharField(label=("Contraseña nueva"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_pass2 = forms.CharField(label=("Repita contraseña nueva"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_pass', 'new_pass1', 'new_pass2')




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

