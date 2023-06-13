from django import forms
from .models import Task, TaskList

class TaskListForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    class Meta:
        model = TaskList
        fields = ['name']

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'})) 
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Description...', 'row':'4'}))
    class Meta:
        model = Task
        fields = ['title', 'body']