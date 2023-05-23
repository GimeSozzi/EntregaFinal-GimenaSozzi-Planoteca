from django import forms
from ckeditor.fields import RichTextField

from app_mensajes.models import Mensaje


class MensajeForm(forms.ModelForm):
    mensaje = RichTextField()
    class Meta:
        model = Mensaje
        fields = ('mensaje',)

    def __init__(self, *args, **kwargs):
        conversacion_id = kwargs.pop('conversacion_id', None)
        emisor = kwargs.pop('emisor_id', None)
        super().__init__(*args, **kwargs)
        self.conversacion_id = conversacion_id
        self.emisor = emisor

    def save(self, commit=True):
        mensaje = super().save(commit=False)
        # mensaje.emisor = self.request.user
        mensaje.conversacion_id = self.conversacion_id
        mensaje.emisor_id = self.emisor
        if commit:
            mensaje.save()
        return mensaje
