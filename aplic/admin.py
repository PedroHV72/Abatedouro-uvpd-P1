from django.contrib import admin

from .models import Endereco, Funcionario, Motorista, Gerente, Estoquista, Revendedora, Frete, Veiculo, Venda, Pedido, Produto, Galeria


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'estado', 'tipo_endereco')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cargo')


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario', 'cnh')


@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario', 'codigo')


@admin.register(Estoquista)
class EstoquistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario', 'codigo')


@admin.register(Revendedora)
class RevendedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')


@admin.register(Frete)
class FreteAdmin(admin.ModelAdmin):
    list_display = ('valor', 'codigo')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'placa', 'cor')


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('codigo_venda', 'valor_total_vendido')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data', 'codigo_pedido', 'status')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo_produto', 'tipo')


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'foto')
