from asyncio import tasks
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def list_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list_tasks.html', {'tasks': tasks})
    # return render(request, 'list_tasks.html')


def create_task(request):
    # print(request.POST)
    Task(title=request.POST['title'],
         description=request.POST['description']).save()
    return redirect('list_tasks')


def delete_task(request, task_id):
    # print(task_id)
    Task.objects.get(id=task_id).delete()
    return redirect('list_tasks')
