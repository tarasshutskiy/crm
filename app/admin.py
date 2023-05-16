from django.contrib import admin

from app.models import ComentCrm, Order, StatusCrm

admin.site.register(ComentCrm)


class CommentAdmin(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_dt', 'coment_name',)
    readonly_fields = ('coment_dt',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt',)
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    inlines = [CommentAdmin, ]


@admin.register(StatusCrm)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
