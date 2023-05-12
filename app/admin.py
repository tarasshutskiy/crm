from django.contrib import admin
from app.models import Order, StatusCrm, ComentCrm

# Register your models here.

admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)