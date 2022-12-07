from django.shortcuts import render, redirect 
from django.contrib import messages

from .models import Todo
from . forms import TodoForm
# Create your views here.
def index(request):
    alltodos = Todo.objects.all().filter(display=True)
    pending = Todo.objects.all().filter(display=True, pending=True)
    completed = Todo.objects.all().filter(display=True, completed=True)

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Task added successfully!')
            return redirect('index')

    context ={
        'alltodos': alltodos,
        'form': form,
        'pending': pending,
        'completed': completed,
    }
    return render(request, 'index.html', context)


def completed(request):
    if request.method == 'POST':
        compbtn = request.POST['complete']
        deltodo = Todo.objects.get(pk=compbtn)
        deltodo.pending = False
        deltodo.completed = True
        deltodo.save()
        messages.success(request, 'Task Completed!')
    return redirect('index')


def uncompleted(request):
    if request.method == 'POST':
        compbtn = request.POST['incomplete']
        deltodo = Todo.objects.get(pk=compbtn)
        deltodo.pending = True
        deltodo.completed = False
        deltodo.save()
        messages.success(request, 'Task not completed yet!')
    return redirect('index')



def deltodo(request):
    if request.method == 'POST':
        delbtn = request.POST['delbtn']
        deltodo = Todo.objects.get(pk=delbtn)
        deltodo.display = False
        deltodo.save()
        messages.success(request, 'Task deleted successfully!')
    return redirect('index')