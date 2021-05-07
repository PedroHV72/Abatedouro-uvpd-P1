from django.views.generic import TemplateView
from django.views.generic import ListView
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
