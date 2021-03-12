from . import views
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new', views.NewTask.as_view(), name='new'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name='delete'),
    path('edit/<int:pk>', views.EditTask.as_view(), name='edit'),
]
