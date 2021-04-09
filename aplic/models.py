from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    estado = models.CharField('Estado', max_length=40)
    complemento = models.CharField('Complemento', max_length=10)
    numero = models.IntegerField('Número')

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f"{self.rua} / {self.cidade} / {self.estado} / {self.numero}"


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
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Motorista(models.Model):
    cnh = models.CharField('CNH', max_length=11)
    salario = models.CharField('Salário', max_length=10)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'


class Gerente(models.Model):
    codigo = models.CharField('Código', max_length=20)
    salario = models.CharField('Salário', max_length=10)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'


class Estoquista(models.Model):
    codigo = models.CharField('Código', max_length=20)
    salario = models.CharField('Salário', max_length=10)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Estoquista'
        verbose_name_plural = 'Estoquistas'


class Revendedora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)

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
    placa = models.CharField('Placa', max_length=7)
    cor = models.CharField('Cor', max_length=15)
    motorista = models.ForeignKey(Motorista, null=True, on_delete=models.SET_NULL)

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
    # nota fiscal

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.codigo_venda
