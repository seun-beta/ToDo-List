from core.settings import INSTALLED_APPS
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'todo'

INSTALLED_APPS = [
    path('', views.index, name='index')

]