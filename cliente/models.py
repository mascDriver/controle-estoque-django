from django.db import models
from django.urls import reverse


class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11)
    nome_cliente = models.CharField(max_length=50)
    telefone_cliente = models.IntegerField()
    cidade_cliente = models.CharField(max_length=50)
    bairro_cliente = models.CharField(max_length=50)
    rua_cliente = models.CharField(max_length=50)
    numero_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'

    def get_absolute_url(self):
        return reverse('cliente-list')

    def __str__(self):
        return f"{self.nome_cliente} - {self.cpf}"