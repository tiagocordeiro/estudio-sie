# Generated by Django 3.0.4 on 2020-03-08 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'managed': False, 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='os',
            options={'managed': False, 'verbose_name': 'Ordem de Serviço', 'verbose_name_plural': 'Ordens de serviço'},
        ),
    ]
