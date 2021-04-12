from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class FuncionarioView(TemplateView):
    template_name = 'funcionarios.html'
