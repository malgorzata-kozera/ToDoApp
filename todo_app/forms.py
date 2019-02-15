from django import forms
from .models import TodoList
from django.forms import ModelForm

# this is a form which inherit from model (class) TodoList

class TasksForm(ModelForm):

    class Meta:

        model = TodoList
        # form fields

        fields = ['task']

    # changing entry label
    def __init__(self, *args, **kwargs):
        super(TasksForm, self).__init__(*args, **kwargs)
        self.fields['task'].label = 'Enter new task'
