from django.db import models
from django.contrib.auth.models import User

class InfoAdicional(models.Model):
    # Se define una tupla con los pronombres disponibles. El primer elemento es el valor que se almacena en la Base de datos y el segundo se mostrará en el formulario.
    OPCIONES_PRONOMBRES = (
        ('he', 'Él'),
        ('she', 'Ella'),
        ('they', 'Elle'),
        ('other', 'Otros'),
    )
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pronombres = models.CharField(max_length=10, choices=OPCIONES_PRONOMBRES, default='other', null=True, blank=True)


    def __str__(self):
        return f'Información Adicional del Usuario: {self.user}'

    class Meta:
        verbose_name_plural = 'Información Adicional'
        


