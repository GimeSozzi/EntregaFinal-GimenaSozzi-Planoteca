from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from app_usuarios.models import InfoAdicional
from app_usuarios.forms import RegistroFormulario, EditarPerfil


def iniciar_sesion(request):

    if request.method == 'POST':

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            login(request, user)

            InfoAdicional.objects.get_or_create(user=request.user)

            return redirect('app_proyectos:inicio')
        else:
            return render(request, 'app_usuarios/iniciar_sesion.html', {'form': formulario})

    formulario = AuthenticationForm()
    return render(request, 'app_usuarios/iniciar_sesion.html', {'form': formulario})


def registro(request):

    if request.method == 'POST':

        formulario = RegistroFormulario(request.POST)

        if formulario.is_valid():
            formulario.save()

            return redirect('app_usuarios:iniciar_sesion')
        else:
            return render(request, 'app_usuarios/registro.html', {'form': formulario})

    formulario = RegistroFormulario()
    return render(request, 'app_usuarios/registro.html', {'form': formulario})


@login_required
def editar_perfil(request):

    if request.method == 'POST':

        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)

        if formulario.is_valid():

            if formulario.cleaned_data.get('avatar'):
                request.user.infoadicional.avatar = formulario.cleaned_data.get('avatar')
            request.user.infoadicional.save()
            formulario.save()
            return redirect('app_proyectos:inicio')
        else:
            return render(request, 'app_usuarios/editar_perfil.html', {'form': formulario})

    formulario = EditarPerfil(initial={'avatar': request.user.infoadicional.avatar}, instance=request.user)
    return render(request, 'app_usuarios/editar_perfil.html', {'form': formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'app_usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('app_usuarios:editar_perfil')
