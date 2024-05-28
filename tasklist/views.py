from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
from .models import Manager

# https://qna.habr.com/q/236166
# https://dev-gang.ru/article/kak-razvernut-prilozhenie-django-v-heroku-s-pomosczu-git-cli-oclmngimkd/

# Create your views here.
def index(request):
    task = Manager.objects.all()
    return render(request, 'manager/index.html', {"task_list": task, 'title': 'HOME PAGE'})


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