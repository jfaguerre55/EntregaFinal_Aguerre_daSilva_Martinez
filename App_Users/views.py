from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
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
    template_name= 'App_Services/editar-perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'App_Services/password-cambio.html'
    success_url = reverse_lazy('password_exitoso')


def password_exitoso(request):
    return render(request, 'App_Services/password-exitoso.html', {})


class AvatarCreate(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = FormularioCreateAvatar
    success_url = reverse_lazy('editar-perfil')
    template_name = 'App_Services/avatar-create.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AvatarCreate, self).form_valid(form)



class AvatarUpdate(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = FormularioUpdateAvatar
    success_url = reverse_lazy('editar-perfil')
    context_object_name = 'avatar'
    template_name = 'App_Services/avatar-update.html'
