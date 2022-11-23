import datetime
from multiprocessing import context
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ToDoListForm
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_data = Task.objects.filter(user = request.user)
    context = {
        'list_task' : task_data,
        'user' : request.user
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register_todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login_todolist.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

def create_task(request):
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST.get('title')
            description = request.POST.get('description')
            todo = Task(user = user, title = title, description = description)
            todo.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            return response
    else:
        form = ToDoListForm()

    return render(request, 'task_create.html', {'form':form})

def change_status(request, pk):
    if Task.objects.get(pk=pk).is_finished == True:
        Task.objects.filter(pk=pk).update(is_finished = False)
    else:
        Task.objects.filter(pk=pk).update(is_finished = True)
    return redirect('todolist:show_todolist')

def delete(request, pk):
    Task.objects.filter(pk=pk).delete()
    return redirect('todolist:show_todolist')