from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Proyecto(models.Model):
    OPCIONES_TIPOLOGIAS = (
        ('vivienda unifamiliar', 'Vivienda Unifamiliar'),
        ('vivienda colectiva', 'Vivienda Colectiva'),
        ('duplex', 'Duplex'),
        ('edificio residencial', 'Edificio Residencial'),
        ('edificio comercial ', 'Edificio Comercial'),
        ('edificio oficinal', 'Edificio Oficinas')
    )
    titulo = models.CharField(max_length=30)
    tipologia = models.CharField(max_length=30,choices=OPCIONES_TIPOLOGIAS, default='vivienda unifamiliar', null=True, blank=True) 
    superficie = models.FloatField()
    plantas = models.IntegerField()
    dormitorios = models.IntegerField()
    banios = models.IntegerField(verbose_name='baños')
    portada = models.ImageField(upload_to='portadas', null=True, blank=True)
    memoria_descriptiva = RichTextField()
    planos = models.FileField(upload_to='planos', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Titulo: {self.titulo} | Tipologia: {self.tipologia} | Autor: {self.autor}'

    class Meta:
        verbose_name_plural = 'Proyectos'
