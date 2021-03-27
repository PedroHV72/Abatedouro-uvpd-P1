from django.db import models


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
    telefone = models.CharField('Telefone', max_length=11, help_text='DD NNNNN-NNNN')
    cargo = models.CharField('Cargo', max_length=40, choices=OPCOES)
    salario = models.DecimalField('Salário', max_digits=10, decimal_places=2)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome


class Motorista(Funcionario):
    cnh = models.CharField('CNH', max_length=11)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'


class Gerente(Funcionario):
    codigo = models.CharField('Código', max_length=20)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'


class Estoquista(Funcionario):
    codigo = models.CharField('Código', max_length=20)

    class Meta:
        verbose_name = 'Estoquista'
        verbose_name_plural = 'Estoquistas'


class Revendedora(Endereco):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=15)

    class Meta:
        verbose_name = 'Revendedora'
        verbose_name_plural = 'Revendedoras'

    def __str__(self):
        return self.nome


class Frete(Endereco):
    valor = models.DecimalField('Valor', max_digits=7, decimal_places=2)
    codigo = models.CharField('Código', max_length=20)

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
