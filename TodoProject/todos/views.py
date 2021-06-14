from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import CreateUserForm, TodoUpdateForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/todos/list/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form': form}
        return render(request, 'todos/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/todos/list/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/todos/list/')
            else:
                messages.info(request, 'Username or Password is incorrect')
                
        context = {}
        return render(request, 'todos/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/todos/login/')

@login_required(login_url='/todos/login/')
def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()} 
    return render(request, 'todos/todo_list.html', context)

@login_required(login_url='/todos/login/')
def insert_todo_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

@login_required(login_url='/todos/login/')
def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')

@login_required(login_url='/todos/login/')
def edit_todo_item(request, todo_id):
    todo_to_edit = Todo.objects.get(id=todo_id)
    todo_to_edit.edit()
    return redirect('/todos/list/')

@login_required(login_url='/todos/login/')
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    context = {
        'form': form
    }
    return render(request, "todos/todo_update.html", context)

