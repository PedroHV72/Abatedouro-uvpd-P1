from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Endereco(models.Model):
    ENDERECOS = (
        ('Funcionário', 'Funcionário'),
        ('Revendedora', 'Revendedora'),
    )
    rua = models.CharField('Rua', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    estado = models.CharField('Estado', max_length=40)
    complemento = models.CharField('Complemento', max_length=10, blank=True)
    numero = models.IntegerField('Número')
    tipo_endereco = models.CharField('Tipo de Endereço', max_length=40, choices=ENDERECOS)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f"{self.rua} / {self.cidade} / {self.estado} / {self.numero} / {self.tipo_endereco}"


class Funcionario(models.Model):
    OPCOES = (
        ('Motorista', 'Motorista'),
        ('Estoquista', 'Estoquista'),
        ('Gerente', 'Gerente'),
    )
    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    telefone = models.CharField('Número celular', max_length=11, help_text='DD NNNNN-NNNN')
    cargo = models.CharField('Cargo', max_length=40, choices=OPCOES)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.CASCADE)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    idade = models.IntegerField('Idade')
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Motorista(Funcionario):
    cnh = models.CharField('CNH', max_length=11)
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'


class Gerente(Funcionario):
    codigo = models.CharField('Código', max_length=20)
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'


class Estoquista(Funcionario):
    codigo = models.CharField('Código', max_length=20)
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Estoquista'
        verbose_name_plural = 'Estoquistas'


class Revendedora(Endereco):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=15)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Revendedora'
        verbose_name_plural = 'Revendedoras'

    def __str__(self):
        return self.nome


class Frete(models.Model):
    valor = models.CharField('Valor', max_length=7)
    codigo = models.CharField('Código', max_length=20)
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Frete'
        verbose_name_plural = 'Fretes'


class Veiculo(models.Model):
    MARCAS = (
        ('Volvo', 'Volvo'),
        ('Scania', 'Scania'),
        ('Volkswagen', 'Volkswagen'),
    )
    placa = models.CharField('Placa', max_length=7)
    cor = models.CharField('Cor', max_length=15)
    marca = models.CharField('Marca', max_length=50, choices=MARCAS)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.placa


class Venda(models.Model):
    codigo_venda = models.IntegerField('Código da venda')
    valor_total_vendido = models.IntegerField('Valor total da venda')
    codigo_frete = models.ForeignKey(Frete, on_delete=models.DO_NOTHING)
    codigo_revendedora = models.ForeignKey(Revendedora, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.codigo_venda


class Produto(models.Model):
    TIPO = (
        ('Coxa', 'Coxa'),
        ('Peito', 'Peito'),
        ('Sobrecoxa', 'Sobrecoxa'),
        ('Asa', 'Asa'),
        ('Coração', 'Coração'),
    )
    tipo = models.CharField('Tipo do produto', max_length=20, choices=TIPO)
    codigo_produto = models.IntegerField('Código do produto')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.tipo


class CaixaTransporte(models.Model):
    codigo_caixa = models.IntegerField('Código da caixa')
    quantidade_caixas = models.IntegerField('Total de caixas')
    peso_total_caixa = models.FloatField('Peso total da caixa')
    codigo_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Caixa de Transporte'
        verbose_name_plural = 'Caixas de Transporte'

    def __str__(self):
        return self.codigo_caixa


class Pedido(models.Model):
    STATUS = (
        ('Pedido aceito', 'Pedido aceito'),
        ('Pedido recusado', 'Pedido recusado'),
    )
    data = models.DateField('Data')
    codigo_pedido = models.IntegerField('Código do pedido')
    status = models.CharField('Status', max_length=20, choices=STATUS)
    valor_total_pedido = models.FloatField('Valor total do pedido')
    codigo_venda = models.ForeignKey(Venda, on_delete=models.DO_NOTHING)
    codigo_caixa = models.ForeignKey(CaixaTransporte, on_delete=models.DO_NOTHING)
    # nota fiscal

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.codigo_pedido
