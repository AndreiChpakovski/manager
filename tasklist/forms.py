from django import forms
from .models import Task, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_complete']