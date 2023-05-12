from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField(max_length=200, verbose_name='Price')
    pc_description = models.CharField(max_length=200, verbose_name='Description')

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return self.pc_value


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Services')
    pt_old_price = models.CharField(max_length=200, verbose_name='Old price')
    pt_new_price = models.CharField(max_length=200, verbose_name='New price')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.pt_title
