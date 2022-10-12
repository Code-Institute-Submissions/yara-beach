from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="cart"),
    path('add/<item_id>/',views.add_to_cart, name="add_to_cart"),
    path('update/<item_id>/',views.update_cart, name="cart_update")
]