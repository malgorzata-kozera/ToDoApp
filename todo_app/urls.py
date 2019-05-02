from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('todolist/', views.todo_list, name='todo-list'),
    path('addnew/', views.add_new_task, name='add-new'),
    path('complete/<one_task_id>', views.task_done, name ='complete'),
    path('uncompleted/<one_task_id>', views.task_undone, name ='uncompleted'),
    path('deletedone/', views.delete_completed_tasks, name='delete-done'),
    path('delete/<one_task_id>', views.delete_task, name='delete-task'),
    path('deleteall/', views.delete_all_tasks, name='delete-all'),
]
