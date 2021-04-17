from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    estado = models.CharField('Estado', max_length=40)
    complemento = models.CharField('Complemento', max_length=10, blank=True)
    numero = models.IntegerField('Número')
    cep = models.CharField('CEP', max_length=9)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f"{self.logradouro} / {self.cidade} / {self.estado}"


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    telefone = models.CharField('Número celular', max_length=13, help_text='DD NNNNN-NNNN')
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.DO_NOTHING)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    data_nasc = models.DateField('Data de Nascimento')
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

    def __str__(self):
        return self.cnh


class Gerente(Funcionario):
    codigo = models.CharField('Código', max_length=20)
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

    def __str__(self):
        return self.codigo


class Estoquista(Funcionario):
    codigo = models.CharField('Código', max_length=20)
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Estoquista'
        verbose_name_plural = 'Estoquistas'

    def __str__(self):
        return self.codigo


class Revendedora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=15)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.DO_NOTHING)
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

    def __str__(self):
        return self.codigo


class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=7)
    cor = models.CharField('Cor', max_length=15)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.placa


class Produto(models.Model):
    TIPO = (
        ('Coxa', 'Coxa'),
        ('Peito', 'Peito'),
        ('Sobrecoxa', 'Sobrecoxa'),
        ('Asa', 'Asa'),
        ('Coração', 'Coração'),
    )
    tipo = models.CharField('Tipo do produto', max_length=20, choices=TIPO)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    codigo_produto = models.IntegerField('Código do produto')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.tipo


class Pedido(models.Model):
    STATUS = (
        ('Aceito', 'Aceito'),
        ('Recusado', 'Recusado'),
    )
    codigo_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade_produto = models.IntegerField('Quantidade do produto')
    data = models.DateField('Data')
    codigo_pedido = models.CharField('Código do pedido', max_length=10)
    status = models.CharField('Status', max_length=20, choices=STATUS)
    valor_total_pedido = models.FloatField('Valor total do pedido')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.codigo_pedido


class Venda(models.Model):
    codigo_venda = models.CharField('Código da venda', max_length=10)
    codigo_pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    codigo_revendedora = models.ForeignKey(Revendedora, on_delete=models.DO_NOTHING)
    cnh_motorista = models.ForeignKey(Motorista, on_delete=models.DO_NOTHING)
    placa_veiculo = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    valor_total_vendido = models.CharField('Valor total da venda', max_length=10)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.codigo_venda


class Galeria(models.Model):
    nome = models.CharField('Nome da foto', max_length=50)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 1100, 'height': 700, 'crop': True}})

    class Meta:
        verbose_name = 'Foto da Galeria'
        verbose_name_plural = 'Fotos da Galeria'

    def __str__(self):
        return self.nome
