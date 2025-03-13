from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views import generic
from .models import Publicacion, Profesor, Materia
from .forms import PublicacionForm

# Create your views here.
class PublicacionView(generic.ListView):
    template_name = 'publicacion/index.html'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:6]
    
class ProfesorView(generic.ListView):
    template_name = 'publicacion/profesor.html'

    def get_queryset(self):
        return Publicacion.objects.filter(profesor_id=self.kwargs['profesor_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesor = get_object_or_404(Profesor, pk=self.kwargs['profesor_id'])
        publicaciones = self.get_queryset()

        # Calcular los promedios
        promedios = publicaciones.aggregate(
            promedio_dominio=Avg('dominio'),
            promedio_puntualidad=Avg('puntualidad'),
            promedio_asistencia=Avg('asistencia'),
            promedio_dificultad=Avg('dificultad'),
            promedio_seguimiento=Avg('seguimiento')
        )

        if publicaciones.exists():
            calificacion_general = (
                promedios['promedio_dominio'] +
                promedios['promedio_puntualidad'] +
                promedios['promedio_asistencia'] +
                promedios['promedio_dificultad'] +
                promedios['promedio_seguimiento']
            ) / 5
        else:
            calificacion_general = 0

        context['profesor'] = profesor
        context['promedio_dominio'] = promedios['promedio_dominio']
        context['promedio_puntualidad'] = promedios['promedio_puntualidad']
        context['promedio_asistencia'] = promedios['promedio_asistencia']
        context['promedio_dificultad'] = promedios['promedio_dificultad']
        context['promedio_seguimiento'] = promedios['promedio_seguimiento']
        context['calificacion_general'] = calificacion_general

        return context
    
class MateriaView(generic.ListView):
    template_name = 'publicacion/materia.html'
    
    def get_queryset(self):
        return Publicacion.objects.filter(materia_id=self.kwargs['materia_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materia = get_object_or_404(Materia, pk=self.kwargs['materia_id'])
        
        context['materia'] = materia
        return context

class PublicarView(generic.FormView):
    template_name = 'publicacion/crear_publicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('publicacion:index')
    login_url = reverse_lazy('usuario:inicio')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['nombre_usuario'] = self.request.user.username
        return kwargs

    def form_valid(self, form):
        publicacion = form.save(commit=False)
        publicacion.usuario = self.request.user  # Asignar el usuario autenticado
        publicacion.save()
        return super().form_valid(form)

