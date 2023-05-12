from django.shortcuts import render
from django.views.generic.list import ListView
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from cms.forms import OrderForms
from app.models import Order
from telebot.sendmessage import sendTelegram


# class CmsListView(ListView):
#     template_name = 'app/index.html'
#     model = CmsSlider
#     context_object_name = 'slider_list'
#

def main_page(requast):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForms()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                }
    return render(requast, 'app/index.html', dict_obj)


def thanks_page(requast):
    if requast.POST:
        name = requast.POST['name']
        phone = requast.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(requast, 'app/thanks.html', {'name': name, })
    else:
        return render(requast, 'app/thanks.html')
