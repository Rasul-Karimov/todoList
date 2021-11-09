from django.shortcuts import render
# Create your views here.
from .models import ToDo


def homepage(request):
    return render(request, 'main/index.html',)


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'main/test.html', {"todo_list": todo_list})
