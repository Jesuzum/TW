from django.db import models

# Create your models here.
class Profesor(models.Model):
    METODOS_ENSENANZA = [
        ('visual', 'Visual'),
        ('auditivo', 'Auditivo'),
        ('kinestesico', 'Kinestésico'),
    ]
    nombre = models.CharField(max_length=50)
    metodo_ensenanza = models.CharField(
        max_length=20,
        choices=METODOS_ENSENANZA,
        default='visual'
    )
    usuarios = models.ManyToManyField('usuario.Usuario', through='publicacion.Publicacion')
    materias = models.ManyToManyField('materia.Materia', through='publicacion.Publicacion')

    def __str__(self) -> str:
        return self.nombre
