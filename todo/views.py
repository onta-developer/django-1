from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/_task_list.html', {'tasks': tasks})

@require_POST
def add_tasks(request):
    title = request.POST.get('title')
    if Task.objects.filter(title=title).exists():
        return HttpResponse('Task already exists')
    else:
        if title:
            Task.objects.create(title=title)
    tasks = Task.objects.all()
    return render(request, 'todo/_task_list.html', {'tasks': tasks})
    # if request.method == 'POST':  
    #     task = Task(title=request.POST['title'])
    #     task.save()
    #     return redirect('home') 

@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    tasks = Task.objects.all()
    return render(request, 'todo/_task_list.html', {'tasks': tasks})


@require_POST
def completed_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    tasks = Task.objects.all()
    return render(request, 'todo/_task_list.html', {'tasks': tasks})