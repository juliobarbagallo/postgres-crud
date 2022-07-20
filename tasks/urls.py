from django.urls import path
from .views import create_task, list_tasks

urlpatterns = [
    path('', list_tasks, name='list_tasks'),
    path('add/', create_task, name='create_task'),
]
