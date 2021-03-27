from django.contrib import admin

from .models import Endereco, Funcionario, Motorista, Gerente, Estoquista, Revendedora, Frete, Veiculo


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'estado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cargo')


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('salario', 'cnh')


@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ('salario', 'codigo')


@admin.register(Estoquista)
class EstoquistaAdmin(admin.ModelAdmin):
    list_display = ('salario', 'codigo')


@admin.register(Revendedora)
class RevendedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')


@admin.register(Frete)
class FreteAdmin(admin.ModelAdmin):
    list_display = ('valor', 'codigo')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'cor')
