from django.conf.urls import url, include
from django.urls import path
from .views import *
from .views_api import *
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('dishes/add/', AddDish.as_view(), name='add_dish_to_order'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish'),
]