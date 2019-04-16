from django.shortcuts import render, redirect
from .forms import TasksForm
from .models import TodoList
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

# Create your views here.


def index(request):

    return render(request, 'todo_app/index.html')

# decorator which makes that user can see this views only when he is login


@login_required
def todo_list(request):

    user = request.user
    # user can see only his own tasks
    tasks_list = TodoList.objects.filter(author=user)

    form = TasksForm()
    context = {'form': form, 'tasks_list': tasks_list}

    return render(request, 'todo_app/todo_list.html', context)


@login_required
@require_POST
def add_new_task(request):

    form = TasksForm(request.POST)
    if form.is_valid():
        task_text = form.cleaned_data.get('task')
        new_task = TodoList(author=request.user, task=task_text)
        new_task.save()
        return redirect('todo-list')

# view which changes selected task as an completed
@login_required
def task_done(request, one_task_id):

    one_task = TodoList.objects.get(pk=one_task_id)

    one_task.complete = True
    one_task.save()
    return redirect('todo-list')

# view which changes selected task as an uncompleted
@login_required
def task_undone(request, one_task_id):

    one_task = TodoList.objects.get(pk=one_task_id)

    one_task.complete = False
    one_task.save()
    return redirect('todo-list')


@login_required
def delete_task(request):
    user = request.user
    done_task = TodoList.objects.filter(complete=True, author=user)
    done_task.delete()
    messages.success(request, 'Your completed tasks have been removed')
    return redirect('todo-list')


@login_required
def delete_all_tasks(request):
    user = request.user
    all_tasks = TodoList.objects.filter(author=user)
    all_tasks.delete()
    messages.success(request, 'Your all tasks have been removed')
    return redirect('todo-list')
