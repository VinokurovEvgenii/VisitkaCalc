from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_PPC, name='calculate_PPC'),
]