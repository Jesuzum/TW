from django.db.models import Q
from django.views import generic
from .models import Profesor

class ProfesorView(generic.ListView):
    template_name = 'profesor/lista_profesor.html'
    context_object_name = 'profesor_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Profesor.objects.filter(Q(nombre__icontains=query)).order_by('nombre')
        return Profesor.objects.order_by('nombre')
