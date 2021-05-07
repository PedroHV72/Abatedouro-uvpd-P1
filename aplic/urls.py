from django.urls import path

from .views import IndexView, FuncionarioView, RevendedoraView, ProdutoView, ProdutoPedidoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('funcionarios/', FuncionarioView.as_view(), name='funcionarios'),
    path('revendedoras/', RevendedoraView.as_view(), name='revendedoras'),
    path('produtos/', ProdutoView.as_view(), name='produtos'),
    path('pedidos/<int:id>/', ProdutoPedidoView.as_view(), name='pedidos')
]
