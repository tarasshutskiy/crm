from django.urls import path
from cms.views import main_page, thanks_page


urlpatterns = [
    path('', main_page),
    path('thanks/', thanks_page, name='thanks_page'),
]


