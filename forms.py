from django.forms import ModelForm, Form
from dishes.models import Ingredient, Drink, Dish, SortDish, InstanceDish
from django import forms


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price']


class AddDishForm(Form):
    dish_id = forms.IntegerField()
    count = forms.IntegerField()
