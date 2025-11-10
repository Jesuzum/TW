from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    METODOS_APRENDIZAJE = [
        ('visual', 'Visual'),
        ('auditivo', 'Auditivo'),
        ('kinestesico', 'Kinestésico'),
    ]
    nombre_usuario = models.CharField(max_length=20)
    metodo_aprendizaje = models.CharField(
        max_length=20,
        choices=METODOS_APRENDIZAJE,
        blank=True,
        null=True
    )
    profesores = models.ManyToManyField('profesor.Profesor', through='publicacion.Publicacion')
    materias = models.ManyToManyField('materia.Materia', through='publicacion.Publicacion')

    def __str__(self):
        return self.username
