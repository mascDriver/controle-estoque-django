from django.db import models
from produtos.models import Produto
from cliente.models import Cliente
from django.urls import reverse


class Venda(models.Model):
    cod_venda = models.AutoField(primary_key=True)
    data_venda = models.DateField()
    valor_total_venda = models.FloatField()
    cpf = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpf', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venda'

    def get_absolute_url(self):
        return reverse('venda-list')
        # return reverse('product-update', kwargs={'pk': self.pk})


class ItensVenda(models.Model):
    cod_item_venda = models.AutoField(primary_key=True)
    quantidade = models.IntegerField()
    valor_unit_venda = models.FloatField()
    cod_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='cod_produto')
    cod_venda = models.ForeignKey(Venda, models.DO_NOTHING, db_column='cod_venda')

    class Meta:
        managed = False
        db_table = 'itens_venda'

    def save(self, *args, **kwargs):
        produto = Produto.objects.get(cod_produto=self.cod_produto.pk)
        produto.quantidade -= self.quantidade
        produto.save()
        super(ItensVenda, self).save(*args, **kwargs)

