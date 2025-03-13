from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre_usuario = models.CharField(max_length=20)
    tipo = models.ImageField(null=True)
    profesores = models.ManyToManyField('profesor.Profesor', through='publicacion.Publicacion')
    materias = models.ManyToManyField('materia.Materia', through='publicacion.Publicacion')