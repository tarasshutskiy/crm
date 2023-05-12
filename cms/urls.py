from django.urls import path
from cms.views import CmsListView


urlpatterns = [
    path('', CmsListView.as_view())
]


