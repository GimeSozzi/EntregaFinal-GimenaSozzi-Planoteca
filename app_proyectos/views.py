from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from app_proyectos.models import Proyecto
from app_proyectos.forms import BuscarProyectoForm
from app_proyectos.forms import ProyectoForm


def inicio(request):
    return render(request, 'app_proyectos/inicio.html')


def buscar_proyecto(request):
    titulo_a_buscar = request.GET.get('titulo', None)
    tipologia_a_buscar = request.GET.get('tipologia', None)

    if titulo_a_buscar:
        proyectos = Proyecto.objects.filter(titulo__icontains=titulo_a_buscar)
    else:
        proyectos = Proyecto.objects.all()

    if tipologia_a_buscar:
        proyectos = proyectos.filter(tipologia__icontains=tipologia_a_buscar)

    formulario_busqueda = BuscarProyectoForm()
    return render(request, 'app_proyectos/buscar_proyecto.html', {'proyectos': proyectos, 'formulario': formulario_busqueda})


def sobre_mi(request):
    foto = 'img/gimena.jpg'
    context = {'foto': foto}
    return render(request, 'app_proyectos/sobre_mi.html', context=context)


class UsuarioEsAutorMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        # Obtener el proyecto correspondiente al proyecto_id
        self.proyecto = get_object_or_404(Proyecto, pk=kwargs['pk'])
        # Verificar si el usuario actual es el propietario del proyecto
        if self.proyecto.autor != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ListaProyecto(ListView):
    model = Proyecto
    template_name = 'app_proyectos/lista_proyecto.html'
    context_object_name = 'proyectos'


class DetalleProyecto(DetailView):
    model = Proyecto
    template_name = 'app_proyectos/detalle_proyecto.html'


class CrearProyecto(LoginRequiredMixin, CreateView):
    form_class = ProyectoForm
    template_name = 'app_proyectos/crear_proyecto.html'
    success_url = reverse_lazy('app_proyectos:lista_proyecto')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.planos = self.request.FILES.get('planos')
        return super().form_valid(form)


class EditarProyecto(UsuarioEsAutorMixin, UpdateView):
    model = Proyecto
    template_name = 'app_proyectos/editar_proyecto.html'
    fields = ['titulo', 'tipologia', 'superficie', 'plantas', 'dormitorios', 'banios', 'portada', 'memoria_descriptiva', 'planos']
    success_url = reverse_lazy('app_proyectos:lista_proyecto')


class EliminarProyecto(UsuarioEsAutorMixin, DeleteView):
    model = Proyecto
    template_name = 'app_proyectos/eliminar_proyecto.html'
    success_url = reverse_lazy('app_proyectos:lista_proyecto')
