from django.urls import path
from .views import create_task, delete_task, list_tasks, update_task

urlpatterns = [
    path('', list_tasks, name='list_tasks'),
    path('add/', create_task, name='create_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('update/<int:task_id>/', update_task, name='update_task')
]
