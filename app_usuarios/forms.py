from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
        labels = {'username': 'Nombre de Usuario'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(label='Imagen de Perfil', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']
        labels = {'email': 'Correo Electrónico', 'first_name': 'Nombre', 'last_name': 'Apellido', 'avatar': 'Imagen de Perfil'}
