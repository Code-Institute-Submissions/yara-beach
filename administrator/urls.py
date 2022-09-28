from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrator, name="administrator"),
    path('admin-excursion', views.admin_excursions, name="admin-excursion"),
    path('admin-rental', views.admin_rentals, name="admin-rental"),
    path('add_excursion', views.add_excursions, name="add_excursion"),
]