from django.db import models


class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='slider_img/')
    cms_title = models.CharField(max_length=200, verbose_name='Title')
    cms_text = models.CharField(max_length=400, verbose_name='Text')
    cms_css = models.CharField(max_length=200, default='-', verbose_name='CSS class')

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.cms_title
