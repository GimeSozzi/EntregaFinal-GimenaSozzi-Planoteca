from django.urls import path
from django.contrib.auth.views import LogoutView
from app_usuarios import views

app_name = 'app_usuarios'

urlpatterns = [
    path('inciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/cambiar_contrasenia', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='app_usuarios/cerrar_sesion.html'), name='cerrar_sesion'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'), # Prueba para transivo
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'), # Prueba para transivo
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'), # Prueba para transivo
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario') # Prueba para transivo
]
