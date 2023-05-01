from django.urls import path
from app_mensajes import views


app_name = 'app_mensajes'


urlpatterns = [
    path('mensajes/<int:usuario_id>/enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('mensajes/', views.ListaMensaje.as_view(), name='lista_conversacion'),
]
