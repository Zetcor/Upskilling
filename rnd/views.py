from django.shortcuts import render, redirect
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

def task_delete(request, id):
    task_id = id
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

def task_edit(request, id):
    task_id = id
    task = Task.objects.get(id=task_id)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        task_form.save()
        return redirect('/')
    
    context = {
        'task_form': task_form
    }

    return render(request, 'task_edit.html', context)

