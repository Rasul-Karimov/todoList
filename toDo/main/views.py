from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import ToDo


def homepage(request):
    return render(request, 'main/index.html',)


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'main/test.html', {"todo_list": todo_list})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
