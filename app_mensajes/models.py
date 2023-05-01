from django.db import models
from django.contrib.auth.models import User


class Conversacion(models.Model):
    participantes = models.ManyToManyField(User, related_name='conversaciones')

    def __str__(self):
        return f'Conversación: {self.pk}'

    class Meta:
        verbose_name_plural = 'Conversaciones'


class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados',
                               on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Mensaje')
    enviado = models.DateTimeField(auto_now_add=True)
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)

    def __str__(self):
        participantes = ', '.join(str(participante) for participante in self.conversacion.participantes.all())
        return f'Mensaje: {self.pk} | Conversación: {self.conversacion.pk} | Entre Usuarios: {participantes} | Enviado: {self.enviado}'

    class Meta:
        verbose_name_plural = 'Mensajes'
