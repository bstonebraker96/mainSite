from django.urls import path

from . import views

app_name = 'sidon'
urlpatterns = [
    path('', views.index, name='index'),
]