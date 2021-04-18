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
    endereco = models.ManyToManyField(Endereco)
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
        return f"{self.id} / {self.nome}"


class Gerente(Funcionario):
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Estoquista(Funcionario):
    salario = models.CharField('Salário', max_length=10)

    class Meta:
        verbose_name = 'Estoquista'
        verbose_name_plural = 'Estoquistas'

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Revendedora(models.Model):
    cnpj = models.IntegerField('CNPJ', unique=True)
    nome = models.CharField('Nome', max_length=50)
    endereco = models.ManyToManyField(Endereco)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Revendedora'
        verbose_name_plural = 'Revendedoras'

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=7)
    cor = models.CharField('Cor', max_length=15)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.placa


class Produto(models.Model):
    nome = models.CharField('Nome do produto', max_length=55)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    disponibilidade = models.BooleanField('Disponibilidade')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Pedido(models.Model):
    STATUS = (
        ('Aceito', 'Aceito'),
        ('Recusado', 'Recusado'),
    )
    produto_id = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    revendedora_id = models.ForeignKey(Revendedora, on_delete=models.DO_NOTHING)
    quantidade_produto = models.IntegerField('Quantidade do produto')
    data = models.DateField('Data')
    status = models.CharField('Status', max_length=20, choices=STATUS)
    valor_total_pedido = models.FloatField('Valor total do pedido')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"{self.id} / {self.revendedora_id} / {self.data}"


class ProdutoPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    produto_id = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)


class Venda(models.Model):
    pedido_id = models.ManyToManyField(Pedido)
    revendedora_id = models.ForeignKey(Revendedora, on_delete=models.DO_NOTHING)
    valor_total_vendido = models.CharField('Valor total da venda', max_length=10)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return f"{self.id} / {self.valor_total_vendido} / {self.revendedora_id}"


class Entrega(models.Model):
    data_entrega = models.DateField('Data da Entrega')
    melhor_horario = models.TimeField('Melhor horário para entrega')
    valor_entrega = models.CharField('Valor frete', max_length=7)
    venda = models.ForeignKey(Venda, on_delete=models.DO_NOTHING)
    motorista = models.ForeignKey(Motorista, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

    def __str__(self):
        return f"{self.id} / {self.data_entrega} / {self.melhor_horario} / {self.motorista} / {self.valor_entrega}"


class Galeria(models.Model):
    nome = models.CharField('Nome da foto', max_length=50)
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 1100, 'height': 700, 'crop': True}})

    class Meta:
        verbose_name = 'Foto da Galeria'
        verbose_name_plural = 'Fotos da Galeria'

    def __str__(self):
        return self.nome
