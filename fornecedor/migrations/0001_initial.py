# Generated by Django 3.2.8 on 2021-10-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('cod_compra', models.AutoField(primary_key=True, serialize=False)),
                ('data_compra', models.DateField()),
            ],
            options={
                'db_table': 'compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('cnpj', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome_fantasia', models.CharField(max_length=50)),
                ('razao_social', models.CharField(max_length=50)),
                ('ie', models.IntegerField()),
                ('email_fornecedor', models.CharField(max_length=100)),
                ('telefone_fornecedor', models.IntegerField()),
                ('cidade_fornecedor', models.CharField(max_length=50)),
                ('bairro_fornecedor', models.CharField(max_length=50)),
                ('rua_fornecedor', models.CharField(max_length=50)),
                ('numero_fornecedor', models.IntegerField()),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': False,
            },
        ),
    ]
