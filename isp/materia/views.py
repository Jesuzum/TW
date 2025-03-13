from django.db.models import Q
from django.views import generic
from .models import Materia

class MateriaView(generic.ListView):
    template_name = "materia/lista_materia.html"
    context_object_name = 'materia_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Materia.objects.filter(Q(nombre__icontains=query)).order_by('clave')
        return Materia.objects.order_by('clave')
