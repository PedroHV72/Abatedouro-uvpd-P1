# Generated by Django 2.2.19 on 2021-04-18 02:38

import aplic.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('estado', models.CharField(max_length=40, verbose_name='Estado')),
                ('complemento', models.CharField(blank=True, max_length=10, verbose_name='Complemento')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('telefone', models.CharField(help_text='DD NNNNN-NNNN', max_length=13, verbose_name='Número celular')),
                ('foto', stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('facebook', models.CharField(blank=True, max_length=200, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=200, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=200, verbose_name='Instagram')),
                ('endereco', models.ManyToManyField(to='aplic.Endereco')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome da foto')),
                ('foto', stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Foto da Galeria',
                'verbose_name_plural': 'Fotos da Galeria',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_produto', models.IntegerField(verbose_name='Quantidade do produto')),
                ('data', models.DateField(verbose_name='Data')),
                ('status', models.CharField(choices=[('Aceito', 'Aceito'), ('Recusado', 'Recusado')], max_length=20, verbose_name='Status')),
                ('valor_total_pedido', models.FloatField(verbose_name='Valor total do pedido')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55, verbose_name='Nome do produto')),
                ('foto', stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Revendedora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.IntegerField(unique=True, verbose_name='CNPJ')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('foto', stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto')),
                ('facebook', models.CharField(blank=True, max_length=200, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=200, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=200, verbose_name='Instagram')),
                ('endereco', models.ManyToManyField(to='aplic.Endereco')),
            ],
            options={
                'verbose_name': 'Revendedora',
                'verbose_name_plural': 'Revendedoras',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, verbose_name='Placa')),
                ('cor', models.CharField(max_length=15, verbose_name='Cor')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
        migrations.CreateModel(
            name='Estoquista',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.Funcionario')),
                ('salario', models.CharField(max_length=10, verbose_name='Salário')),
            ],
            options={
                'verbose_name': 'Estoquista',
                'verbose_name_plural': 'Estoquistas',
            },
            bases=('aplic.funcionario',),
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.Funcionario')),
                ('salario', models.CharField(max_length=10, verbose_name='Salário')),
            ],
            options={
                'verbose_name': 'Gerente',
                'verbose_name_plural': 'Gerentes',
            },
            bases=('aplic.funcionario',),
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.Funcionario')),
                ('cnh', models.CharField(max_length=11, verbose_name='CNH')),
                ('salario', models.CharField(max_length=10, verbose_name='Salário')),
            ],
            options={
                'verbose_name': 'Motorista',
                'verbose_name_plural': 'Motoristas',
            },
            bases=('aplic.funcionario',),
        ),
        migrations.CreateModel(
            name='ProdutoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Pedido')),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Produto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='revendedora_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Revendedora'),
        ),
        migrations.CreateModel(
            name='Frete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=7, verbose_name='Valor')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Endereco')),
            ],
            options={
                'verbose_name': 'Frete',
                'verbose_name_plural': 'Fretes',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total_vendido', models.CharField(max_length=10, verbose_name='Valor total da venda')),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Pedido')),
                ('placa_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Veiculo')),
                ('revendedora_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Revendedora')),
                ('cnh_motorista', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Motorista')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
