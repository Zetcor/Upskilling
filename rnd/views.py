from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def index(request):
    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            task_form = TaskForm()

    tasks = Task.objects.all()
    context = {
        'name': 'Thaddeus Toledo',
        'task_form': task_form,
        'tasks': tasks
    }
    return render(request, 'index.html', context)


