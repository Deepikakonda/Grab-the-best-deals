from django.urls import path
from . import views

app_name = 'deals'

urlpatterns = [
    path('', views.home, name='home'),
    path('groceries/', views.groceries, name='groceries'),
    path('deals_all/search/', views.groceries_search, name='groceries_search'),
    path('stationeries/', views.stationeries, name='stationeries'),
    path('furnitures/', views.furnitures, name='furnitures'),
    path('gadgets/', views.gadgets, name='gadgets'), 
]
