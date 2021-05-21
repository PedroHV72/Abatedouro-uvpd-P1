from django.db import models
from stdimage.models import StdImageField
import uuid
from django.utils.translation import gettext_lazy as _


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Endereco(models.Model):
    logradouro = models.CharField(_('Logradouro'), max_length=50)
    cidade = models.CharField(_('Cidade'), max_length=50)
    bairro = models.CharField(_('Bairro'), max_length=50)
    estado = models.CharField(_('Estado'), max_length=40)
    complemento = models.CharField(_('Complemento'), max_length=10, blank=True)
    numero = models.IntegerField(_('Número'))
    cep = models.CharField(_('CEP'), max_length=9)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    def __str__(self):
        return f"{self.logradouro} / {self.cidade} / {self.estado}"


class Funcionario(models.Model):
    nome = models.CharField(_('Nome'), max_length=50)
    cpf = models.CharField(_('CPF'), max_length=11)
    telefone = models.CharField(_('Número celular'), max_length=13, help_text='DD NNNNN-NNNN')
    endereco = models.ManyToManyField(Endereco)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    data_nasc = models.DateField(_('Data de Nascimento'))
    facebook = models.CharField(_('Facebook'), blank=True, max_length=200)
    twitter = models.CharField(_('Twitter'), blank=True, max_length=200)
    instagram = models.CharField(_('Instagram'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome


class Motorista(Funcionario):
    cnh = models.CharField(_('CNH'), max_length=11)
    salario = models.CharField(_('Salário'), max_length=10)

    class Meta:
        verbose_name = _('Motorista')
        verbose_name_plural = _('Motoristas')

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Gerente(Funcionario):
    salario = models.CharField(_('Salário'), max_length=10)

    class Meta:
        verbose_name = _('Gerente')
        verbose_name_plural = _('Gerentes')

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Estoquista(Funcionario):
    salario = models.CharField(_('Salário'), max_length=10)

    class Meta:
        verbose_name = _('Estoquista')
        verbose_name_plural = _('Estoquistas')

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Revendedora(models.Model):
    cnpj = models.IntegerField(_('CNPJ'), unique=True)
    nome = models.CharField(_('Nome'), max_length=50)
    endereco = models.ManyToManyField(Endereco)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    facebook = models.CharField(_('Facebook'), blank=True, max_length=200)
    twitter = models.CharField(_('Twitter'), blank=True, max_length=200)
    instagram = models.CharField(_('Instagram'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Revendedora')
        verbose_name_plural = _('Revendedoras')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(_('Nome do produto'), max_length=55)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 870, 'height': 1110, 'crop': True}})
    disponibilidade = models.BooleanField(_('Disponibilidade'))

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Pedido(models.Model):
    STATUS = (
        ('Aceito', _('Aceito')),
        ('Recusado', _('Recusado')),
    )
    produto_id = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    revendedora_id = models.ForeignKey(Revendedora, on_delete=models.DO_NOTHING)
    quantidade_produto = models.IntegerField(_('Quantidade do produto'))
    data = models.DateField(_('Data'))
    status = models.CharField(_('Status'), max_length=20, choices=STATUS)
    valor_total_pedido = models.FloatField(_('Valor total do pedido'))

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')

    def __str__(self):
        return f"{self.id} / {self.revendedora_id} / {self.data}"


class ProdutoPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    produto_id = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)


class Venda(models.Model):
    pedido_id = models.ManyToManyField(Pedido)
    revendedora_id = models.ForeignKey(Revendedora, on_delete=models.DO_NOTHING)
    valor_total_vendido = models.CharField(_('Valor total da venda'), max_length=10)

    class Meta:
        verbose_name = _('Venda')
        verbose_name_plural = _('Vendas')

    def __str__(self):
        return f"{self.id} / {self.valor_total_vendido} / {self.revendedora_id}"


class Entrega(models.Model):
    data_entrega = models.DateField(_('Data da Entrega'))
    melhor_horario = models.TimeField(_('Melhor horário para entrega'))
    valor_entrega = models.CharField(_('Valor frete'), max_length=7)
    venda = models.ForeignKey(Venda, on_delete=models.DO_NOTHING)
    motorista = models.ForeignKey(Motorista, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Entrega')
        verbose_name_plural = _('Entregas')

    def __str__(self):
        return f"{self.id} / {self.data_entrega} / {self.melhor_horario} / {self.motorista} / {self.valor_entrega}"


class Galeria(models.Model):
    nome = models.CharField(_('Nome da foto'), max_length=50)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 1100, 'height': 700, 'crop': True}})

    class Meta:
        verbose_name = _('Foto da Galeria')
        verbose_name_plural = _('Fotos da Galeria')

    def __str__(self):
        return self.nome
