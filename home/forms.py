from django import forms  
from . models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'time']
        widgets ={
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'})
        }
