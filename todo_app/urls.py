from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('todolist/', views.todo_list, name='todo-list'),
    path('addnew/', views.add_new_task, name='add-new'),
    path('complete/<one_task_id>', views.task_done, name ='complete'),
    path('deletedone/', views.delete_task, name='delete-done'),
    path('deleteall/', views.delete_all_tasks, name='delete-all'),
]
