from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiment_list, name='experiment_list'),
    path('about/', views.about, name='about'),
    path('experiment/<slug:slug>/', views.experiment_detail, name='experiment_detail'),
    path('experiment/<slug:slug>/play/', views.simulation_view, name='simulation'),
]
