# Generated by Django 2.2.19 on 2021-04-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='tipo_endereco',
            field=models.CharField(choices=[('Funcionário', 'Funcionário'), ('Revendedora', 'Revendedora')], max_length=40, verbose_name='Tipo de Endereço'),
        ),
    ]