from django.urls import path
from . import views

app_name = 'materia'

urlpatterns = [
    path('lista_materia/', views.MateriaView.as_view(), name='lista_materia'),
]
