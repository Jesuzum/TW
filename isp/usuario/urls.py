from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuario'

urlpatterns = [
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('test-aprendizaje/', views.TestAprendizajeView.as_view(), name='test_aprendizaje'),
    path('inicio/', views.InicioView.as_view(), name='inicio'),
    path('cerrar/', auth_views.LogoutView.as_view(next_page='usuario:inicio'), name='cerrar'),
]
