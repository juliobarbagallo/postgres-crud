from django.shortcuts import render

# Create your views here.


def list_tasks(request):
    return render(request, 'list_tasks.html')
