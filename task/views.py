from xmlrpc.server import resolve_dotted_attribute

from django.shortcuts import render
from .models import Works
from.forms import WorkForm
from django.shortcuts import redirect , get_object_or_404
from .models import Works
# Create your views here.

def task_list(request):
    tasks = Works.objects.filter(is_deleted = False)
    form = WorkForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    
    return render(request , 'task/task_list.html' , {'tasks' : tasks , 'form':form})

def add_task(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('task_list')

def delete_task(request , task_id):
    task = Works.objects.get(id = task_id)
    task.is_deleted = True
    task.save()
    return redirect('task_list')

