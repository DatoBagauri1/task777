from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.helloooooooo, name='randomname'),
    path('info/', views.info, name='info'),
    path('h/', views.hobby, name='h'),
]
