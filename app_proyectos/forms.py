from django import forms

from app_proyectos.models import Proyecto


class BuscarProyectoForm(forms.Form):
    titulo = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipologia = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'tipologia', 'superficie', 'plantas', 'dormitorios', 'banios', 'portada', 'memoria_descriptiva', 'planos']
