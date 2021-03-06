# Generated by Django 3.2.8 on 2021-10-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cod_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_usuario', models.CharField(max_length=50)),
                ('email_usuario', models.CharField(max_length=100, unique=True)),
                ('senha_usuario', models.CharField(max_length=500)),
                ('is_superuser', models.BooleanField(null=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
