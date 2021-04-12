from django.views.generic import TemplateView
from .models import Funcionario


class IndexView(TemplateView):
    template_name = 'index.html'


class FuncionarioView(TemplateView):
    template_name = 'funcionarios.html'

    def get_context_data(self, **kwargs):
        context = super(FuncionarioView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('nome').all()
        return context
