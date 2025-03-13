from django.urls import path
from . import views

app_name = 'publicacion'
urlpatterns = [
    path('', views.PublicacionView.as_view(), name='index'),
    path('publicar/', views.PublicarView.as_view(), name='crear_publicacion'),
    path('profesor/<int:profesor_id>', views.ProfesorView.as_view(), name='profesor'),
    path('materia/<int:materia_id>', views.MateriaView.as_view(), name='materia'),
]