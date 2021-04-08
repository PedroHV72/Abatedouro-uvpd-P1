# Generated by Django 2.2.19 on 2021-04-08 18:11

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto'),
        ),
    ]