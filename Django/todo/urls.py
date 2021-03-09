from . import views
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new', views.TaskNew.as_view(), name='new'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete'),
    path('edit/<int:pk>', views.TaskEdit.as_view(), name='edit'),
]
