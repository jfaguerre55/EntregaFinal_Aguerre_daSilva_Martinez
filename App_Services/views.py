from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Servicio, Comentario
from .forms import *



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
    context_object_name = 'impresion3d'
    queryset = Servicio.objects.filter(servicio__startswith='impresion3d')
    template_name = 'App_Services/impresion3d-lista.html'
    login_url = '/login/'

class Impresion3DDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'impresion3d'
    template_name = 'App_Services/impresion3d-detalle.html'

class Impresion3DUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('impresion3d-lista')
    context_object_name = 'impresion3d'
    template_name = 'App_Services/impresion3d-editar.html'

class Impresion3DDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('impresion3d-lista')
    context_object_name = 'impresion3d'
    template_name = 'App_Services/impresion3d-borrar.html'


# ESCANEO 3D

class Escaneo3DLista(LoginRequiredMixin, ListView):
    context_object_name = 'escaneo3d'
    queryset = Servicio.objects.filter(servicio__startswith='escaneo3d')
    template_name = 'App_Services/escaneo3d-lista.html'
    login_url = '/login/'

class Escaneo3DDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'escaneo3d'
    template_name = 'App_Services/escaneo3d-detalle.html'

class Escaneo3DUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('escaneo3d-lista')
    context_object_name = 'escaneo3d'
    template_name = 'App_Services/escaneo3d-editar.html'

class Escaneo3DDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('escaneo3d-lista')
    context_object_name = 'escaneo3d'
    template_name = 'App_Services/escaneo3d-borrar.html'


# SOFTWARE

class SoftwareLista(LoginRequiredMixin, ListView):
    context_object_name = 'software'
    queryset = Servicio.objects.filter(servicio__startswith='software')
    template_name = 'App_Services/software-lista.html'
    login_url = '/login/'

class SoftwareDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'software'
    template_name = 'App_Services/software-detalle.html'

class SoftwareUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('software-lista')
    context_object_name = 'software'
    template_name = 'App_Services/software-editar.html'

class SoftwareDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('software-lista')
    context_object_name = 'software'
    template_name = 'App_Services/software-borrar.html'



# OTRO

class OtrosLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Servicio.objects.filter(servicio__startswith='otro')
    template_name = 'App_Services/otros-lista.html'
    login_url = '/login/'

class OtrosDetalle(LoginRequiredMixin, DetailView):
    model = Servicio
    context_object_name = 'otros'
    template_name = 'App_Services/otros-detalle.html'

class OtrosUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ActualizacionServicio
    success_url = reverse_lazy('otros-lista')
    context_object_name = 'otros'
    template_name = 'App_Services/otros-editar.html'

class OtrosDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('otros-lista')
    context_object_name = 'otros'
    template_name = 'App_Services/otros-borrar.html'




