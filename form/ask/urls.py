from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('3/', views.done),
]
