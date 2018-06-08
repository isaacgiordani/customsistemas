# Generated by Django 2.0.5 on 2018-06-08 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listatelefonica', '0002_auto_20180606_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=35, verbose_name='Descrição')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Acesso',
                'verbose_name_plural': 'Acessos',
            },
        ),
        migrations.CreateModel(
            name='AccessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=35, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'AcessoTipo',
                'verbose_name_plural': 'AcessoTipos',
            },
        ),
        migrations.AddField(
            model_name='access',
            name='accesstype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listatelefonica.AccessType', verbose_name='AcessoTipo'),
        ),
        migrations.AddField(
            model_name='access',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listatelefonica.Entity', verbose_name='Entidade'),
        ),
    ]