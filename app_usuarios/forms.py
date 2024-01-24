from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # Prueba para transivo

from app_usuarios.models import InfoAdicional



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
    pronombres = forms.ChoiceField(label='Pronombres', choices=InfoAdicional.OPCIONES_PRONOMBRES, widget=forms.Select(attrs={'class': 'form-control'}), initial='other')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'pronombres']
        labels = {'email': 'Correo Electrónico', 'first_name': 'Nombre', 'last_name': 'Apellido', 'avatar': 'Imagen de Perfil', 'pronombres': 'Pronombres'}

# Prueba para transivo
class CrearUsuarioFormulario(UserCreationForm):
    nombre_completo = forms.CharField(max_length=100, label='Nombre Completo')
    grupo = forms.ChoiceField(choices=[('admin', 'Administradores'), ('operador', 'Operadores')], label='Grupo')
    
    class Meta:
        model = User
        fields = ['nombre_completo', 'username', 'password1', 'password2', 'grupo']
        
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditarUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'groups']
     