from django import forms
from .models import Task

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['date','title','description']