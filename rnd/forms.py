from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {

            'title': forms.TextInput(attrs = {
                'id': 'task-title',
                'placeholder': 'Enter task title...',
                'class': 'w-full border py-1 px-2 rounded'
            }),

            'description': forms.Textarea(attrs = {
                'id': 'task-description',
                'placeholder': 'Enter task description...',
                'class': 'w-full border py-1 px-2 rounded'
            })
        }