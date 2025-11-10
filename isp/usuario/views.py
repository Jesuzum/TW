from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth import views
from .forms import RegistroForm
from .tests_aprendizaje import TEST_PREGUNTAS, calcular_metodo


class RegistroView(generic.FormView):
    template_name = 'usuario/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuario:test_aprendizaje')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('publicacion:index')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return redirect(self.success_url)


class TestAprendizajeView(LoginRequiredMixin, View):
    template_name = 'usuario/test_aprendizaje.html'

    def get(self, request):
        return render(request, self.template_name, {'preguntas': TEST_PREGUNTAS})

    def post(self, request):
        respuestas = []
        for i in range(len(TEST_PREGUNTAS)):
            respuesta = request.POST.get(f'pregunta_{i}')
            if respuesta:
                respuestas.append(respuesta)

        metodo = calcular_metodo(respuestas)
        usuario = request.user
        usuario.metodo_aprendizaje = metodo
        usuario.save()

        return redirect('publicacion:index')


class InicioView(views.LoginView):
    template_name = 'usuario/inicio_sesion.html'
    redirect_authenticated_user = True
    next_page = 'publicacion:index'
