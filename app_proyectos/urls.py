from django.urls import path
from app_proyectos import views


app_name = 'app_proyectos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('proyectos/', views.ListaProyecto.as_view(), name='lista_proyecto'),
    path('proyectos/buscar/', views.buscar_proyecto, name='buscar_proyecto'),
    path('proyectos/crear/', views.CrearProyecto.as_view(), name='crear_proyecto'),
    path('proyectos/<int:pk>/', views.DetalleProyecto.as_view(), name='detalle_proyecto'),
    path('proyectos/<int:pk>/editar/', views.EditarProyecto.as_view(), name='editar_proyecto'),
    path('proyectos/<int:pk>/eliminar/', views.EliminarProyecto.as_view(), name='eliminar_proyecto'),
]
