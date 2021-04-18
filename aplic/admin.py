from django.contrib import admin

from .models import Endereco, Funcionario, Motorista, Gerente, Estoquista, Revendedora, Entrega, Venda, Pedido, Produto, Galeria


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'cidade', 'estado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario', 'cnh')


@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'salario')


@admin.register(Estoquista)
class EstoquistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'salario')


@admin.register(Revendedora)
class RevendedoraAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome')


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor_entrega')


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor_total_vendido')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'status')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'foto')
