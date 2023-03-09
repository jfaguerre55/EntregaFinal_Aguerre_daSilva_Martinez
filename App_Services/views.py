from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
#from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Servicio, Comentario
from .forms import *

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'App_Services/home.html'


class LoginPagina(LoginView):
    template_name = 'App_Services/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class RegistroPagina(FormView):
    template_name = 'App_Services/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)


class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'App_Services/edicion-perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'App_Services/password-cambio.html'
    success_url = reverse_lazy('password_exitoso')


def password_exitoso(request):
    return render(request, 'App_Services/password-exitoso.html', {})



# CREACION SERVICIO

class ServicioCreacion(LoginRequiredMixin, CreateView):
    model = Servicio
    form_class = FormularioNuevoServicio
    success_url = reverse_lazy('home')
    template_name = 'App_Services/servicio-creacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ServicioCreacion, self).form_valid(form)


# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'App_Services/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)


# ACERCA DE NOSOTROS
def about(request):
    return render(request, 'App_Services/acerca-de-nosotros.html', {})



# IMPRESION 3D

class Impresion3DLista(LoginRequiredMixin, ListView):
    context_object_name = 'impresion3d-lista'
    queryset = Servicio.objects.filter(instrumento__startswith='impresion3d')
    template_name = 'App_Services/impresion3d-lista.html'
    login_url = '/login/'

class Impresion3DDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'impresion3d-detalle'
    template_name = 'App_Services/impresion3d-detalle.html'

class Impresion3DUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('impresion3d-lista')
    context_object_name = 'impresion3d-editar'
    template_name = 'App_Services/impresion3d-editar.html'

class Impresion3DDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('impresion3d-lista')
    context_object_name = 'impresion3d-detalle'
    template_name = 'App_Services/impresion3d-borrar.html'


# ESCANEO 3D

class Escaneo3DLista(LoginRequiredMixin, ListView):
    context_object_name = 'escaneo3d-lista'
    queryset = Servicio.objects.filter(instrumento__startswith='escaneo3d')
    template_name = 'App_Services/escaneo3d-lista.html'
    login_url = '/login/'

class Escaneo3DDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'escaneo3d-detalle'
    template_name = 'App_Services/escaneo3d-detalle.html'

class Escaneo3DUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('escaneo3d-lista')
    context_object_name = 'escaneo3d-editar'
    template_name = 'App_Services/escaneo3d-editar.html'

class Escaneo3DDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('escaneo3d-lista')
    context_object_name = 'escaneo3d-detalle'
    template_name = 'App_Services/escaneo3d-borrar.html'


# SOFTWARE

class SoftwareLista(LoginRequiredMixin, ListView):
    context_object_name = 'software-lista'
    queryset = Servicio.objects.filter(instrumento__startswith='software')
    template_name = 'App_Services/software-lista.html'
    login_url = '/login/'

class SoftwareDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'software-detalle'
    template_name = 'App_Services/software-detalle.html'

class SoftwareUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('software-lista')
    context_object_name = 'software-editar'
    template_name = 'App_Services/software-editar.html'

class SoftwareDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('software-lista')
    context_object_name = 'software-detalle'
    template_name = 'App_Services/software-borrar.html'



# OTRO

class OtrosLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros-lista'
    queryset = Servicio.objects.filter(servicio__startswith='otros')
    template_name = 'App_Services/otros-lista.html'
    login_url = '/login/'

class OtrosDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'otros-detalle'
    template_name = 'App_Services/otros-detalle.html'

class OtrosUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('otros-lista')
    context_object_name = 'otros-editar'
    template_name = 'App_Services/otros_editar.html'

class OtrosDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('otros-lista')
    context_object_name = 'otros-detalle'
    template_name = 'App_Services/otros_eliminar.html'




