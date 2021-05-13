from django.db.models import Count
from django.views.generic import TemplateView
from django.views.generic import ListView
from chartjs.views.lines import BaseLineChartView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django_weasyprint import WeasyTemplateView
from weasyprint import HTML
from .models import Funcionario, Revendedora, Galeria, Produto, Pedido


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['foto'] = Galeria.objects.order_by('nome').all()
        return context


class FuncionarioView(TemplateView):
    template_name = 'funcionarios.html'

    def get_context_data(self, **kwargs):
        context = super(FuncionarioView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('nome').all()
        return context


class RevendedoraView(TemplateView):
    template_name = 'revendedoras.html'

    def get_context_data(self, **kwargs):
        context = super(RevendedoraView, self).get_context_data(**kwargs)
        context['revendedoras'] = Revendedora.objects.order_by('nome').all()
        return context


class ProdutoView(TemplateView):
    template_name = 'encomendas.html'

    def get_context_data(self, **kwargs):
        context = super(ProdutoView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.order_by('?').all()
        return context


class ProdutoPedidoView(ListView):
    template_name = 'pedidos.html'
    model = Pedido
    paginate_by = 5
    ordering = 'nome'

    def get_context_data(self, **kwargs):
        context = super(ProdutoPedidoView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['produtos'] = Produto.objects.filter(id=id).first
        return context

    def get_queryset(self):
        id = self.kwargs['id']
        return Pedido.objects.filter(produto_id=id)


class DadosGraficoPedidosView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = Produto.objects.order_by('id')
        for produto in queryset:
            labels.append(produto.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Produto.objects.order_by('id').annotate(total=Count('pedido'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado


class RelatorioPedidosView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.order_by('id')

        html_string = render_to_string('relatorio-pedidos.html', {'pedidos': pedidos})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-pedidos.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-pedidos.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-pedidos.pdf"'
        return response
