from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse


from app_usuarios.models import InfoAdicional
from app_usuarios.forms import RegistroFormulario, EditarPerfil
from app_usuarios.forms import CrearUsuarioFormulario # Prueba para transivo
from app_usuarios.forms import EditarUsuarioForm # Prueba para transivo
from app_usuarios.decorators import admin_or_superuser_only # Prueba para transivo


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
def perfil(request):
    
    usuario = request.user
    info_adicional = InfoAdicional.objects.get_or_create(user=request.user)

    contexto = {'usuario': usuario, 'info_adicional': info_adicional}
    
    return render(request, 'app_usuarios/perfil.html', contexto)


@login_required
def editar_perfil(request):

    if request.method == 'POST':

        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)

        if formulario.is_valid():

            if formulario.cleaned_data.get('avatar'):
                request.user.infoadicional.avatar = formulario.cleaned_data.get('avatar')
                
            if formulario.cleaned_data.get('pronombres'):
                request.user.infoadicional.pronombres = formulario.cleaned_data.get('pronombres')
                
            request.user.infoadicional.save()
            
            formulario.save()
            return redirect('app_usuarios:perfil')
        else:
            return render(request, 'app_usuarios/editar_perfil.html', {'form': formulario})

    formulario = EditarPerfil(initial={'avatar': request.user.infoadicional.avatar, 'pronombres': request.user.infoadicional.pronombres}, instance=request.user)
    return render(request, 'app_usuarios/editar_perfil.html', {'form': formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'app_usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('app_usuarios:editar_perfil')


# Prueba para transivo

@admin_or_superuser_only # Asegura que el usuario pertenece al grupo Administradores o es un superuser
def crear_usuario(request):
    # if not request.user.is_staff:  # Verifica si el usuario no es un administrador
    #     return redirect('app_usuarios:perfil')  # Redirige a la página de perfil 

    if request.method == 'POST':
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
            # Crear un nuevo usuario con los datos proporcionados
            nuevo_usuario = formulario.save(commit=False)
            nuevo_usuario.set_password(formulario.cleaned_data['password1'])
            nuevo_usuario.save()

            # Asignar el usuario al grupo correspondiente (Administradores u Operadores)
            if formulario.cleaned_data['grupo'] == 'admin':
                grupo_administradores = Group.objects.get(name='Administradores')
                grupo_administradores.user_set.add(nuevo_usuario)
            elif formulario.cleaned_data['grupo'] == 'operador':
                grupo_operadores = Group.objects.get(name='Operadores')
                grupo_operadores.user_set.add(nuevo_usuario)

            return redirect('app_usuarios:lista_usuarios')  # Redirige a la página con el listado de usuarios
 
    else:
        formulario = CrearUsuarioFormulario()

    return render(request, 'app_usuarios/crear_usuario.html', {'formulario': formulario})


@admin_or_superuser_only
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'app_usuarios/lista_usuarios.html', {'usuarios': usuarios})


@admin_or_superuser_only
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    
    if request.method == 'POST':
        formulario = EditarUsuarioForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('app_usuarios:lista_usuarios')  # Redirige de vuelta a la lista de usuarios después de la edición

    else:
        formulario = EditarUsuarioForm(instance=usuario)

    return render(request, 'app_usuarios/editar_usuario.html', {'formulario': formulario})


@admin_or_superuser_only
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('app_usuarios:lista_usuarios')  # Redirige de vuelta a la lista de usuarios después de la eliminación

    return render(request, 'app_usuarios/eliminar_usuario.html', {'usuario': usuario})

