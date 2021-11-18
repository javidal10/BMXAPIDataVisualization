from django import urls
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('',views.get_dates,name='info'),
    path('data',views.home, name='home'),
]

