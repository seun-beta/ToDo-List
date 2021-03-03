from core.settings import INSTALLED_APPS
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('edit/<int:number>', views.Edit.as_view(), name='edit'),
    path('new', views.New.as_view(), name='new'),
    path('success', views.Success.as_view(), name='success')

]
