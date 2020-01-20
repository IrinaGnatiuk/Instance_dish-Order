from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.views.generic import ListView, View, TemplateView, DetailView
from django.views.generic.edit import FormView, UpdateView
from dishes.models import *
from order.models import Order
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms import *
from .serialisers import *
from dishes.cache import get_client_ip
from project.celery import add


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/dish.html'


class AddDish(FormView):
    form_class = AddDishForm
    template_name = 'dishes/dishes_add_form.html'
    success_url = '/order/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_dish'] = Dish.objects.all()
        context['list_instance_dish'] = InstanceDish.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        return Dish.objects.all()

    def form_valid(self, form):
        dish = Dish.objects.get(id=form.cleaned_data.get('dish_id'))
        id = form.cleaned_data.get('dish_id')
        instance_dish = InstanceDish.objects.filter(dish_template=id)
        count = form.cleaned_data.get('count')
        if instance_dish:
            instance_dish = InstanceDish.objects.get(dish_template=id)
            instance_dish.count += count
            instance_dish.save()
        else:
            instance_dish = dish.create_instance_dish(count)
        if not self.request.user.is_authenticated:
            order = Order.objects.first()
            order.dishes.add(instance_dish)
        else:
            order, created = Order.objects.get_or_create(user=self.request.user)
            order.dishes.add(instance_dish)
        order.get_full_price()
        return super().form_valid(form)
