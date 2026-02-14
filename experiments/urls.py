from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiment_list, name='experiment_list'),
    path('experiment/<slug:slug>/play/', views.simulation_view, name='simulation'),
]
