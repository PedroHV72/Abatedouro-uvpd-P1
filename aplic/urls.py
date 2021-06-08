from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import IndexView, FuncionarioView, RevendedoraView, ProdutoView, ProdutoPedidoView, \
    DadosGraficoPedidosView, RelatorioPedidosView, ContatoView, FuncionarioViewSet, RevendedoraViewSet, GaleriaViewSet,\
    ProdutoViewSet, PedidoViewSet


router = SimpleRouter()
router.register('funcionarios', FuncionarioViewSet)
router.register('revendedoras', RevendedoraViewSet)
router.register('galeria', GaleriaViewSet)
router.register('produtos', ProdutoViewSet)
router.register('pedidos', PedidoViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', IndexView.as_view(), name='index'),
    path('funcionarios/', FuncionarioView.as_view(), name='funcionarios'),
    path('revendedoras/', RevendedoraView.as_view(), name='revendedoras'),
    path('produtos/', ProdutoView.as_view(), name='produtos'),
    path('pedidos/<int:id>/', ProdutoPedidoView.as_view(), name='pedidos'),
    path('dados-grafico-pedidos/', DadosGraficoPedidosView.as_view(), name='dados-grafico-pedidos'),
    path('relatorio-pedidos/', RelatorioPedidosView.as_view(), name='relatorio-pedidos'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('auth/', include('rest_framework.urls'))
]
