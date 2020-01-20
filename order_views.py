from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView, FormView
from order.models import Order, ShippingOrder
from accounts.models import User
from dishes.models import InstanceDish
from order.forms import OrderForm, ShippingOrderForm, EditCountDish
from django.http import HttpResponseRedirect, HttpResponse


class OrderView(TemplateView):
    model = Order
    template_name = "order/order.html"
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            order = Order.objects.first()
        else:
            order, created = Order.objects.get_or_create(user=self.request.user)
        return context

    def get_queryset(self):
        return Order.objects.all()

    def del_dish_from_order(self, pk):
        order = Order.objects.first()
        dish = order.dishes.get(id=pk)
        dish.delete()
        order.get_full_price()
        return HttpResponseRedirect("/order")
