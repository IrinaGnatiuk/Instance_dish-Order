from django.conf.urls import url, include
from django.urls import path
from . import views
# from order.views import MakeOrder

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),
    path('del_dish/<int:pk>/', views.OrderView.del_dish_from_order, name='delete_dish_from_order'),
]