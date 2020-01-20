from django.forms import ModelForm, Form
from dishes.models import Ingredient, Drink, Dish, SortDish, InstanceDish
from order.models import Order, ShippingOrder
from django import forms


class OrderForm(ModelForm):
    instance_dish = forms.CharField(max_length=250)
    user = forms.CharField(max_length=250)
    full_price = forms.DecimalField(required=True, max_digits=2, decimal_places=9)

    class Meta:
        model = Order
        fields = ['dishes', 'full_price', 'user']
