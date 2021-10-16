from django.db import models
from django.urls import reverse
from cliente.models import Cliente


class Produto(models.Model):
    cod_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    descr_produto = models.CharField(max_length=255)
    valor_unit = models.FloatField()
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'produto'

    def get_absolute_url(self):
        return reverse('product-list')
        # return reverse('product-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.cod_produto} - {self.nome_produto}"

