from django.urls import path
from .views import list_tasks

urlpatterns = [
    path('', list_tasks, name='list_tasks'),
]
