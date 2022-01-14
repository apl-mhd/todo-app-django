from asyncio import tasks
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm


def index(request):

    tasks = Task.objects.all()

    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'tasks': tasks, 'form':form}

    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'form':form, 'task':task}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')



    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):

    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('list')

    return render(request, 'tasks/delete.html', context)