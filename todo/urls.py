from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('add-tasks/', views.add_tasks, name='add-tasks'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
    path('completed-task/<int:task_id>', views.completed_task, name='completed-task'),
]