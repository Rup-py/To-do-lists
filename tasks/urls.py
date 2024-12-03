from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),  # List and create tasks
    path('tasks/<int:id>/', views.TaskDetailView.as_view(), name='task-detail'),  # View, update, delete tasks
]

