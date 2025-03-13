# forms.py
from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    # nombre_usuario = forms.CharField(
    #     max_length=20, 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    titulo = forms.CharField(
        max_length=30, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    dominio = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)], 
        label="Dominio",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    puntualidad = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)], 
        label="Puntualidad",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    asistencia = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)], 
        label="Asistencia",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    dificultad = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)], 
        label="Dificultad",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    seguimiento = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)], 
        label="Seguimiento",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Publicacion
        fields = ['profesor', 'materia', 'titulo', 'fecha', 'comentario', 'dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento']
        widgets = {
            'profesor': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.Select(attrs={'class': 'form-control'}),
        }
