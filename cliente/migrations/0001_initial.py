# Generated by Django 3.2.8 on 2021-10-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=50)),
                ('telefone_cliente', models.IntegerField()),
                ('cidade_cliente', models.CharField(max_length=50)),
                ('bairro_cliente', models.CharField(max_length=50)),
                ('rua_cliente', models.CharField(max_length=50)),
                ('numero_cliente', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
    ]
