from django.urls import path
from . import views

urlpatterns = [
    path('', views.excursion, name="excursions"),
    path('detail/<int:pk>', views.excursion_details, name="detail"),
    path('add_images/<int:pk>', views.excursion_images, name="add_images"),
    path('form', views.add_excursions, name="form"),
]