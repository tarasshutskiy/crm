from django.db import models


class TeleSettings(models.Model):
    tb_token = models.CharField(max_length=200, verbose_name='Token')
    tb_chat = models.CharField(max_length=200, verbose_name='Chat ID')
    tb_text = models.TextField( verbose_name='Text')

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.tb_chat
