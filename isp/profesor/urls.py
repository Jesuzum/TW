from django.urls import path
from . import views

app_name = 'profesor'

urlpatterns = [
    path('lista_profesor/', views.ProfesorView.as_view(), name='lista_profesor'),
]
