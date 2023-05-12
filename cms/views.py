from django.shortcuts import render
from django.views.generic.list import ListView
from cms.models import CmsSlider


class CmsListView(ListView):
    template_name = 'app/index.html'
    model = CmsSlider
    ordering = ['cms_title']
    context_object_name = 'slider_list'
