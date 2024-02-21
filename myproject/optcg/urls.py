from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random_card/', views.random_card, name='random_card'),
    path('search/', views.search_card, name='search_card'),
    path('search_result/', views.search_result, name='search_result'),
]