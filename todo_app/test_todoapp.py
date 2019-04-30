from django.test import TestCase
import pytest
from todo_app.models import TodoList
from todo_app.forms import TasksForm

from django.contrib.auth.models import User

# Create your tests here.

class TestTasks(TestCase):

    def setUp(self):
        user = User()
        user.username = 'test_user'
        user.email = 'test@mail.com'
        user.save()
        self.user = user

        task = TodoList.objects.create(task='do something',author=self.user, complete=False)
        task.save()
        self.task=task

        done_task = TodoList.objects.create(task='do something',author=self.user, complete=True)
        done_task.save()
        self.done_task = done_task

    def test_save_task_properly(self):

        tasks = TodoList.objects.all()
        self.assertEquals(len(tasks), 2)

        task = tasks[0]
        self.assertEquals(task, self.task)

    def test_tasks_listed_index(self):
        """Test that tasks are listed on task page page for a login user"""
        pass

    def test_delete_completed_tasks(self):
        self.done_task.delete()
        tasks = TodoList.objects.filter(complete=True, author=self.user)
        self.assertEquals(len(tasks), 0)

    def test_delete_just_added_task(self):
        pass
    def test_delete_all_tatsks(self):
        self.task.delete()
        self.done_task.delete()
        tasks = TodoList.objects.all()
        self.assertEquals(len(tasks), 0)

    def test_makred_tasks_as_done(self):
        pass
    def test_makred_tasks_as_undone(self):
        pass
    def test_tasks_form_validation(self):
        """Test that data form is valid, form field can not be empty"""
        form_data = {'task': 'do something'}
        form = TasksForm(data=form_data)
        self.assertTrue(form.is_valid())
