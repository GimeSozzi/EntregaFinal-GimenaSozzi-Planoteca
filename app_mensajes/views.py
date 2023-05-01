from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from app_mensajes.models import Conversacion
from app_mensajes.forms import MensajeForm


def enviar_mensaje(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    conversacion = buscar_conversacion(request.user, usuario)
    mensajes = conversacion.mensaje_set.all()

    if request.method == 'POST':
        form = MensajeForm(request.POST, conversacion_id=conversacion.id, emisor_id=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('app_mensajes:enviar_mensaje', usuario_id=usuario.id)
    else:
        form = MensajeForm(conversacion_id=conversacion.id, emisor_id=request.user.id)

    contexto = {'conversacion': conversacion, 'mensajes': mensajes, 'form': form, 'usuario': usuario}
    return render(request, 'app_mensajes/enviar_mensaje.html', context=contexto)


def buscar_conversacion(usuario1, usuario2):
    # Buscamos una conversación existente entre los usuarios
    conversacion = Conversacion.objects.filter(participantes=usuario1).filter(participantes=usuario2).first()

    # Si no existe la conversación, la creamos
    if not conversacion:
        conversacion = Conversacion.objects.create()
        conversacion.participantes.add(usuario1, usuario2)

    return conversacion


class ListaMensaje(LoginRequiredMixin, ListView):
    model = Conversacion
    template_name = 'app_mensajes/lista_conversacion.html'
    context_object_name = 'conversaciones'

    def get_queryset(self):
        # Obtener el usuario actual
        usuario_actual = self.request.user

        # Filtrar las conversaciones en las que el usuario actual sea un participante
        queryset = Conversacion.objects.filter(participantes__in=[usuario_actual])

        return queryset
