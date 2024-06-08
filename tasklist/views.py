from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
from .models import Manager, Task, Comment
from .forms import TaskForm, CommentForm

# https://qna.habr.com/q/236166
# https://dev-gang.ru/article/kak-razvernut-prilozhenie-django-v-heroku-s-pomosczu-git-cli-oclmngimkd/

# Create your views here.
def index(request):
    task = Manager.objects.all()
    return render(request, 'manager/index.html', {"task_list": task, 'title': 'HOME PAGE'})

def task_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_list')
    else:
        form = CommentForm()
    return render(request, 'tasks/task_list.html', {'task_list': tasks, 'form': form})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments, 'form': form})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    task = Manager(title=title)
    task.save()
    return redirect('index')


def update(request, task_id):
    task = Manager.objects.get(id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('index')


def delete(request, task_id):
    task = Manager.objects.get(id=task_id)
    task.delete()
    return redirect('index')
