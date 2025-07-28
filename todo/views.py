from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/_task_list.html', {'tasks': tasks})