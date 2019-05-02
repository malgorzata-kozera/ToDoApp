import pytest
from django.test import TestCase
from todo_app.models import TodoList
from todo_app.forms import TasksForm


from django.contrib.auth.models import User


# Create your tests here.

class TestTasks(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='testpassword')
        self.user = user

        task = TodoList.objects.create(task='do something', author=self.user, complete=False)
        self.task = task

        done_task = TodoList.objects.create(task='do something', author=self.user, complete=True)
        self.done_task = done_task

    def test_save_task_properly(self):
        """Test that tasks are saved on database properly"""
        tasks = TodoList.objects.all()
        assert len(tasks) == 2
        task = tasks[0]
        assert task == self.task

    def test_tasks_listed_for_selected_user(self):
        """Test that tasks are listed only for selected user"""
        user2 = User.objects.create(username='test3', password='testpassword')
        self.user2 = user2
        task = TodoList.objects.create(task='test message', author=self.user2, complete=False)
        task = TodoList.objects.create(task='test message two', author=self.user2, complete=False)
        assert len(TodoList.objects.filter(author=self.user2)) == 2

    def test_delete_completed_tasks(self):
        assert TodoList.objects.filter(author=self.user, complete=True).exists()
        self.done_task.delete()
        assert not TodoList.objects.filter(author=self.user, complete=True).exists() is True
        assert len(TodoList.objects.filter(author=self.user)) == 1

    def test_delete_selected_task(self):
        assert TodoList.objects.filter(id=1).exists()
        self.task.delete()
        assert not TodoList.objects.filter(id=1).exists() is True

    def test_delete_all_tatsks(self):
        User.objects.create(username='test2', password='testpassword')
        test2 = User.objects.filter(username='test2').first()
        TodoList.objects.create(task='test message three', author=test2, complete=False)
        tasks = TodoList.objects.filter(author=self.user)
        tasks.delete()
        assert len(tasks) == 0
        assert len(TodoList.objects.all()) == 1

    def test_makred_tasks_as_done(self):
        assert TodoList.objects.filter(id=1, author=self.user, complete=False).exists
        selected_task = TodoList.objects.filter(id=1, author=self.user, complete=False)
        selected_task.complete = True
        assert selected_task.complete is True

    def test_makred_tasks_as_undone(self):
        assert TodoList.objects.filter(id=1, author=self.user, complete=True).exists
        selected_task = TodoList.objects.filter(id=1, author=self.user, complete=True)
        selected_task.complete = False
        assert selected_task.complete is False

    def test_tasks_form_validation(self):
        """Test that data form is valid, form field can not be empty"""
        form_data = {'task': 'do something'}
        form = TasksForm(data=form_data)
        assert form.is_valid() is True
