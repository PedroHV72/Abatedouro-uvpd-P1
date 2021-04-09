# Generated by Django 2.2.19 on 2021-04-09 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_venda', models.IntegerField(verbose_name='Código da venda')),
                ('valor_total_vendido', models.IntegerField(verbose_name='Valor total da venda')),
                ('codigo_frete', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Frete')),
                ('codigo_revendedora', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Revendedora')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('codigo_pedido', models.IntegerField(verbose_name='Código do pedido')),
                ('status', models.CharField(choices=[('Pedido aceito', 'Pedido aceito'), ('Pedido recusado', 'Pedido recusado')], max_length=20, verbose_name='Status')),
                ('valor_total_pedido', models.FloatField(verbose_name='Valor total do pedido')),
                ('codigo_venda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Venda')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
